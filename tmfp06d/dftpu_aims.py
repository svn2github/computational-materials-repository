import os
import time

import ase.db
from ase.structure import molecule
from ase.optimize.bfgs import BFGS
from ase.vibrations import Vibrations
from ase.calculators.aims import Aims
from ase.data.tmfp06d import data

c = ase.db.connect('aims.db')

basis = 'tier2'

code = 'aims' + '_' + basis

names = sorted(data.keys())

for name in names:
    id = c.reserve(name=name, basis=basis)
    if id is None:
        continue
    label = name + '_' + code
    atoms = molecule(name, data=data)
    kwargs = {}
    if name in ['O', 'F']:
        sc_accuracy_rho = 5.e-5
        sc_accuracy_eev = 5.e-5
    elif name in ['Sc', 'Ti', 'V', 'Fe', 'Co', 'Ni']:
        sc_accuracy_rho = 2.e-3
        sc_accuracy_eev = 1.e-4
    elif name in ['CoO', 'CrN', 'CrO', 'Fe2', 'FeF', 'FeO', 'Mn2', 'TiO', 'VN']:
        sc_accuracy_rho = 2.e-3
        sc_accuracy_eev = 2.e-3
    else:
        sc_accuracy_rho = 1.e-4
        sc_accuracy_eev = 1.e-3
    kwargs.update({'relativistic': 'none'})
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
                occupation_type=['gaussian', 0.00001],
                override_relativity=True,
                override_illconditioning=True,
                basis_threshold=0.00005,
                charge_mix_param=0.0005,
                sc_iter_limit=19000,
                **kwargs
                )
    atoms.set_calculator(calc)
    t = time.time()
    if len(atoms) > 1:
        # need a copy of atoms for calculation of vibrations
        vibatoms = atoms.copy()
        vibatoms.set_calculator(calc)
        vib = Vibrations(vibatoms, name=label + '_fixed')
        vib.run()
        f = vib.get_frequencies()[-1].real
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=False, basis=basis,
                frequency=f,
                time=time.time()-t)
    else:
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=False, basis=basis,
                time=time.time()-t)
    if len(atoms) > 1:
        opt = BFGS(atoms,
                   logfile=name + '_' + code + '.log',
                   trajectory=name + '_' + code + '.traj')
        t = time.time()
        opt.run(0.005)
        # need a copy of atoms for calculation of vibrations
        vibatoms = atoms.copy()
        vibatoms.set_calculator(calc)
        vib = Vibrations(vibatoms, name=label + '_relaxed')
        vib.run()
        f = vib.get_frequencies()[-1].real
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=True, basis=basis,
                frequency=f,
                time=time.time()-t)
    del c[id]
