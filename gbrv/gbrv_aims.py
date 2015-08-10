import os
import sys
import time

import numpy as np

import ase.db
from ase.utils import opencew
from ase.calculators.calculator import kpts2mp
from ase.io import Trajectory
from ase.calculators.aims import Aims
from ase.test.tasks.gbrv import GBRVBulkCollection as Collection

collection = Collection()

if len(sys.argv) == 1:
    category = 'fcc'
    collection = Collection()
    names = collection.names
elif len(sys.argv) == 2:
    category = sys.argv[1]
    collection = Collection(category=category) 
    names = collection.names
else:
    category = sys.argv[1]
    collection = Collection(category=category) 
    names = [sys.argv[2]]

c = ase.db.connect('gbrv.db')

# select the basis set
#basis = 'light'
#basis = 'tight'
#basis = 'really_tight'
basis = 'tier2'

kptdensity = 16.0
width = 0.01

relativistic = 'none'
relativistic = 1.e-12
relativistic = 'scalar'

if category == 'magnetic_moments':
    charge_mix_param_orig = 0.001
    basis_threshold_orig = 0.0001
    sc_accuracy_rho_orig = 3.e-3
    sc_accuracy_eev_orig = 5.e-3
else:
    charge_mix_param_orig = 0.01
    basis_threshold_orig = 0.00001
    sc_accuracy_rho_orig = 1.e-4
    sc_accuracy_eev_orig = 5.e-3

if relativistic == 'none':
    linspace = (0.92, 1.08, 7)  # eos numpy's linspace
else:
    linspace = (0.98, 1.02, 5)  # eos numpy's linspace
if category == 'magnetic_moments':
    linspace = (1.0, 1.0, 1)  # eos numpy's linspace
linspacestr = ''.join([str(t) + 'x' for t in linspace])[:-1]

code = category + '_aims' + '-' + basis + '_e' + linspacestr
code = code + '_k' + str(kptdensity) + '_w' + str(width)
code = code + '_t' + str(basis_threshold_orig) + '_r' + str(relativistic)

for name in names:
    # save all steps in one traj file in addition to the database
    # we should only used the database c.reserve, but here
    # traj file is used as another lock ...
    fd = opencew(name + '_' + code + '.traj')
    if fd is None:
        continue
    traj = Trajectory(name + '_' + code + '.traj', 'w')
    atoms = collection[name]
    cell = atoms.get_cell()
    kpts = tuple(kpts2mp(atoms, kptdensity, even=True))
    kwargs = {}
    if name in ['MnSbIr', 'NbSbFe', 'NbSbRu', 'RhSbMn', 'PtSbMn', 'PdSbMn']:
        charge_mix_param = 0.01
        basis_threshold = 0.00002
        sc_accuracy_rho = 5.e-4
        sc_accuracy_eev = 5.e-3
    elif category == 'magnetic_moments' and name in ['TcO', 'RuO', 'RhO', 'IrO']:
        charge_mix_param = charge_mix_param_orig
        basis_threshold = 0.0005
        sc_accuracy_rho = sc_accuracy_rho_orig
        sc_accuracy_eev = sc_accuracy_eev_orig
    elif category == 'magnetic_moments' and name in ['VO', 'Os']:
        charge_mix_param = 0.0001
        basis_threshold = 0.0001
        sc_accuracy_rho = sc_accuracy_rho_orig
        sc_accuracy_eev = sc_accuracy_eev_orig
    else:
        charge_mix_param = charge_mix_param_orig
        basis_threshold = basis_threshold_orig
        sc_accuracy_rho = sc_accuracy_rho_orig
        sc_accuracy_eev = sc_accuracy_eev_orig
    if relativistic == 'scalar':
        kwargs.update({'relativistic': ['atomic_zora', relativistic]})
    elif relativistic == 'none':
        kwargs.update({'relativistic': 'none'})
    else:  # e.g. 1.0e-12
        kwargs.update({'relativistic': ['zora', 'scalar', relativistic]})
    if atoms.get_initial_magnetic_moments().any():  # spin-polarization
        magmom = atoms.get_initial_magnetic_moments().sum() / len(atoms)
        kwargs.update({'spin': 'collinear'})
    # loop over EOS linspace
    for n, x in enumerate(np.linspace(linspace[0], linspace[1], linspace[2])):
        id = c.reserve(category=category,
                       name=name, basis=basis, linspacestr=linspacestr,
                       kptdensity=kptdensity, width=width,
                       basis_threshold=basis_threshold,
                       relativistic=relativistic,
                       x=x)
        if id is None:
            continue
        # perform EOS step
        atoms.set_cell(cell * x, scale_atoms=True)
        # set calculator
        atoms.calc = Aims(
            label=name + '_' + code + '_' + str(n),
            species_dir=os.path.join(os.environ['AIMS_SPECIES_DIR'], basis),
            xc='PBE',
            kpts=kpts,
            KS_method='elpa',
            sc_accuracy_rho=sc_accuracy_rho,
            sc_accuracy_eev=sc_accuracy_eev,
            occupation_type=['gaussian', width],
            override_relativity=True,
            override_illconditioning=True,
            basis_threshold=basis_threshold,
            charge_mix_param=charge_mix_param,
            sc_iter_limit=9000,
            )
        atoms.calc.set(**kwargs)  # remaining calc keywords
        t = time.time()
        atoms.get_potential_energy()
        c.write(atoms,
                category=category,
                name=name, basis=basis, linspacestr=linspacestr,
                kptdensity=kptdensity, width=width,
                basis_threshold=basis_threshold,
                relativistic=relativistic,
                x=x,
                magnetic_moment=atoms.calc.get_magnetic_moment(),
                time=time.time()-t)
        traj.write(atoms)
        del c[id]
