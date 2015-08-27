import time

import ase.db
from ase.structure import molecule
from ase.optimize.bfgs import BFGS
from ase.data.g2 import data
from ase.data.g2 import molecule_names, atom_names
from gpaw import GPAW, PW, Mixer, MixerSum, MixerDif

c = ase.db.connect('gpaw.db')

optimize = True

pw = 900

code = 'gpaw' + '_' + str(pw)

names = atom_names + molecule_names

for name in names:
    id = c.reserve(name=name, pw=pw)
    if id is None:
        continue
    label = name + '_' + code
    atoms = molecule(name, data=data)
    atoms.set_cell((12.2,12.1,14.0))
    atoms.center()
    kwargs = {}
    if atoms.get_initial_magnetic_moments().any():  # spin-polarization
        mixer = Mixer(0.05, 5)
        kwargs.update({'fixmom': True})
    else:
        mixer = Mixer(0.05, 5)
    if len(atoms) == 1:
        kwargs.update({'hund': True})
    else:
        kwargs.update({'hund': False})
    calc = GPAW(
        mode=PW(pw),
        xc='PBE',
        width=0,
        convergence={'eigenstates': 5.e-9},
        mixer=mixer,
        maxiter=1777,
        txt=label + '.txt',
        **kwargs)
    t = time.time()
    atoms.set_calculator(calc)
    atoms.get_potential_energy()
    c.write(atoms, name=name, relaxed=False, pw=pw,
            time=time.time()-t)
    if optimize and len(atoms) > 1:
        opt = BFGS(atoms,
                   logfile=name + '_' + code + '.log',
                   trajectory=name + '_' + code + '.traj')
        t = time.time()
        opt.run(0.005)
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=True, pw=pw,
                time=time.time()-t)
    del c[id]
