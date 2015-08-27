import os
import time

import ase.db
from ase.structure import molecule
from ase.optimize.bfgs import BFGS
from ase.calculators.nwchem import NWChem
from ase.data.g2 import data
from ase.data.g2 import molecule_names, atom_names

c = ase.db.connect('nwchem.db')

basis = 'def2-qzvppd'

code = 'nwchem' + '_' + basis

names = atom_names + molecule_names

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
                  #basis='* library aug-cc-pv5z except Li Be Na\nLi library aug-cc-pvqz\nBe library aug-cc-pvqz\nNa library aug-cc-pvqz\n',
                  basispar='spherical',
                  direct='noio',
                  raw='set int:txs:limxmem 20485760208\nmemory total 20000 Mb noverify\n',
                  label=label)
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
