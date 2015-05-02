import os
import time

import ase.db
from ase.structure import molecule
from ase.optimize.bfgs import BFGS
from ase.vibrations import Vibrations
from ase.calculators.nwchem import NWChem
from ase.data.tmfp06d import data

c = ase.db.connect('nwchem.db')

basis = 'def2-qzvppd'

code = 'nwchem' + '_' + basis

names = sorted(data.keys())

for name in names:
    id = c.reserve(name=name, basis=basis)
    if id is None:
        continue
    label = name + '_' + code
    atoms = molecule(name, data=data)
    calc = NWChem(geometry='noautosym nocenter noautoz',
                  task='gradient',
                  xc='PBE',
                  grid='nodisk',
                  tolerances='tight',
                  maxiter=777,
                  convergence={'lshift': 0.0},
                  basis=basis,
                  basispar='spherical',
                  direct='noio',
                  raw='set int:txs:limxmem 134217728\nmemory total 8000 Mb noverify\n',
                  label=label)
    atoms.set_calculator(calc)
    t = time.time()
    if len(atoms) > 1:
        # need a copy of atoms for calculation of vibrations
        vibatoms = atoms.copy()
        vibatoms.set_calculator(calc)
        vib = Vibrations(vibatoms, name=label + '_fixed')
        vib.run()
        f = vib.get_frequencies()[-1].real
        # clean nwchem restart
        if os.path.exists(name + '_' + code + '.db'):
            os.remove(name + '_' + code + '.db')
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
        # clean nwchem restart
        if os.path.exists(name + '_' + code + '.db'):
            os.remove(name + '_' + code + '.db')
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=True, basis=basis,
                frequency=f,
                time=time.time()-t)
    del c[id]
