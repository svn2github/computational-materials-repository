import os
import time

import ase.db
from ase.structure import molecule
from ase.units import Rydberg
from ase.optimize.bfgs import BFGS
try:
    from espresso import espresso as espressoORIG
    # modifications needed to the old-style interfaces
    class espresso(espressoORIG):
        name = 'espresso'
        def check_state(self, atoms): return []
        def todict(self): return {}
except ImportError:
    pass
from ase.data.g2 import data
from ase.data.g2 import molecule_names, atom_names

c = ase.db.connect('espresso.db')

pw = 100
dw = 400

code = 'espresso' + '_' + str(pw) + str(dw)

names = atom_names + molecule_names

for name in names:
    id = c.reserve(name=name, pw=pw, dw=dw)
    if id is None:
        continue
    label = name + '_' + code
    atoms = molecule(name, data=data)
    atoms.set_cell((12.2,12.1,14.0))
    atoms.center()
    kwargs = {}
    if atoms.get_initial_magnetic_moments().any():  # spin-polarization
        kwargs.update({'spinpol': True})
        kwargs.update({'fix_magmom': True})
    atoms.calc = espresso(outdir=label,
                          xc='PBE',
                          pw=pw*Rydberg,
                          dw=dw*Rydberg,
                          sigma=0.0,
                          mode='scf',
                          # will overwrite disk_io parameter if True
                          output={'avoidio':True},
                          convergence={'mixing': 0.05, 'maxsteps':500,},
                          dontcalcforces=True,
                          )
    atoms.calc.set(**kwargs)  # remaining calc keywords
    t = time.time()
    atoms.calc.results = {'energy': atoms.get_potential_energy()}
    c.write(atoms, name=name, relaxed=False, pw=pw, dw=dw,
            time=time.time()-t)
    # no optimization: espresso does not conform yet to ASE interface style
    if 0 and len(atoms) > 1:
        opt = BFGS(atoms,
                   logfile=name + '_' + code + '.log',
                   trajectory=name + '_' + code + '.traj')
        t = time.time()
        opt.run(0.005)
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=True, pw=pw, dw=dw,
                time=time.time()-t)
    del c[id]
