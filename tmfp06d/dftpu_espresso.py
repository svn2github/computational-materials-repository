import time

import ase.db
from ase.units import Rydberg
from ase.structure import molecule
from ase.optimize.bfgs import BFGS
from ase.vibrations import Vibrations
from ase.data.tmfp06d import data
from espresso import espresso as espressoORIG

# modifications needed to the old-style interfaces
class espresso(espressoORIG):
    name = 'espresso'
    def check_state(self, atoms): return []
    def todict(self): return {}

c = ase.db.connect('espresso.db')

pw = 100
dw = 400

code = 'espresso' + '_' + 'pw' + str(pw) + 'dw' + str(dw)

names = sorted(data.keys())

for name in names:
    id = c.reserve(name=name, pw=pw, dw=dw)
    if id is None:
        continue
    label = name + '_' + code
    atoms = molecule(name, data=data)
    atoms.set_cell((12.0,12.1,16.0))
    kwargs = {}
    if atoms.get_initial_magnetic_moments().any():  # spin-polarization
        kwargs.update({'spinpol': True})
        kwargs.update({'fix_magmom': True})
    calc = espresso(
        outdir=label,
        xc='PBE',
        kpts=[1,1,1],
        pw=pw*Rydberg,
        dw=dw*Rydberg,
        sigma=0,
        mode='scf',
        output={'avoidio': True},  # will overwrite disk_io parameter if True
        convergence={'mixing': 0.1, 'maxsteps':500,},
        **kwargs)
    t = time.time()
    atoms.set_calculator(calc)
    if len(atoms) > 1:
        # need a copy of atoms for calculation of vibrations
        vibatoms = atoms.copy()
        vibatoms.set_calculator(calc)
        vib = Vibrations(vibatoms, name=label + '_fixed')
        vib.run()
        f = vib.get_frequencies()[-1].real
        e = atoms.get_potential_energy()
        atoms.calc.results = {'energy': e}
        c.write(atoms, name=name, relaxed=False, pw=pw, dw=dw,
                frequency=f,
                time=time.time()-t)
    else:
        e = atoms.get_potential_energy()
        atoms.calc.results = {'energy': e}
        c.write(atoms, name=name, relaxed=False, pw=pw, dw=dw,
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
        e = atoms.get_potential_energy()
        atoms.calc.results = {'energy': e}
        c.write(atoms, name=name, relaxed=True, pw=pw, dw=dw,
                frequency=f,
                time=time.time()-t)
    del c[id]
