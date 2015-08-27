import os
import time

import ase.db
from ase.structure import molecule
from ase.optimize.bfgs import BFGS
from ase.calculators.aims import Aims
from ase.data.g2 import data
from ase.data.g2 import molecule_names, atom_names

c = ase.db.connect('aims.db')

basis = 'tight'
basis_threshold = 0.00001

code = 'aims' + '_' + basis

names = atom_names + molecule_names

for name in names:
    id = c.reserve(name=name, basis=basis)
    if id is None:
        continue
    label = name + '_' + code
    atoms = molecule(name, data=data)
    kwargs = {}
    # I'm not aware of a reliable way of avoiding
    # fractional occupancies for atoms in FHI-AIMS
    # The results depend on the number of cores, architecture,
    # width, convergence thresholds, ...
    if name in ['N']:
        sc_accuracy_rho = 5.e-5
        sc_accuracy_eev = 5.e-5
        charge_mix_param = 0.0005
        width = 0.00001
    elif name in ['B', 'O', 'F', 'Al', 'Si', 'S', 'Cl', 'CH', 'SH', 'ClO']:
        sc_accuracy_rho = 1.e-4
        sc_accuracy_eev = 5.e-5
        charge_mix_param = 0.0001
        width = 0.0000005
    elif name in ['C']:
        sc_accuracy_rho = 5.e-5
        sc_accuracy_eev = 5.e-5
        charge_mix_param = 0.0005
        width = 0.0000005
    else:
        sc_accuracy_rho = 1.e-4
        sc_accuracy_eev = 1.e-3
        charge_mix_param = 0.0005
        width = 0.00001
    if name == 'SiH2_s3B1d':
        atoms.set_initial_magnetic_moments([5.0, 0.0, 0.0])
    kwargs.update({'relativistic': 'none'})
    #kwargs.update({'relativistic': ['atomic_zora', 'scalar']})
    if atoms.get_initial_magnetic_moments().any():  # spin-polarization
        magmom = atoms.get_initial_magnetic_moments().sum() / len(atoms)
        kwargs.update({'spin': 'collinear'})
    calc = Aims(label=label,
                species_dir=os.path.join(os.environ['AIMS_SPECIES_DIR'], basis),
                xc='PBE',
                KS_method='elpa',
                sc_accuracy_rho=sc_accuracy_rho,
                sc_accuracy_eev=sc_accuracy_eev,
                sc_accuracy_forces=1.e-3,
                occupation_type=['gaussian', width],
                override_relativity=True,
                override_illconditioning=True,
                basis_threshold=basis_threshold,
                charge_mix_param=charge_mix_param,
                sc_iter_limit=19000,
                **kwargs
                )
    atoms.set_calculator(calc)
    t = time.time()
    atoms.get_potential_energy()
    c.write(atoms, name=name, relaxed=False, basis=basis,
            time=time.time()-t)
    if len(atoms) > 1:
        opt = BFGS(atoms,
                   logfile=name + '_' + code + '.log',
                   trajectory=name + '_' + code + '.traj')
        t = time.time()
        opt.run(0.005)
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=True, basis=basis,
                time=time.time()-t)
    del c[id]
