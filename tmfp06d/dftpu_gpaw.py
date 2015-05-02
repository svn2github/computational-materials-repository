import time

import ase.db
from ase.structure import molecule
from ase.optimize.bfgs import BFGS
from ase.vibrations import Vibrations
from ase.data.tmfp06d import data
from gpaw import GPAW, PW, Mixer, MixerSum, RMM_DIIS

c = ase.db.connect('gpaw.db')

pw = 700

code = 'gpaw' + '_' + str(pw)

names = sorted(data.keys())

for name in names:
    id = c.reserve(name=name, pw=pw)
    if id is None:
        continue
    label = name + '_' + code
    atoms = molecule(name, data=data)
    atoms.set_cell((12.0,12.1,16.0))
    kwargs = {}
    if atoms.get_initial_magnetic_moments().any():
        if len(atoms) == 1:
            kwargs.update({'mixer': MixerSum(0.01, 1)})
            kwargs.update({'fixmom': True})
        else:
            kwargs.update({'mixer': MixerSum(0.005, 5)})
            kwargs.update({'fixmom': True})
    else:
        kwargs.update({'mixer': Mixer(0.05, 5)})
    if len(atoms) == 1:
        kwargs.update({'hund': True})
    else:
        kwargs.update({'hund': False})
    calc = GPAW(
        mode=PW(pw),
        xc='PBE',
        width=0,
        convergence={'eigenstates': 5.e-9},
        basis='dzp',
        eigensolver=RMM_DIIS(niter=6),
        maxiter=1777,
        txt=label + '.txt',
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
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=False, pw=pw,
                frequency=f,
                time=time.time()-t)
    else:
        atoms.get_potential_energy()
        c.write(atoms, name=name, relaxed=False, pw=pw,
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
        c.write(atoms, name=name, relaxed=True, pw=pw,
                frequency=f,
                time=time.time()-t)
    del c[id]
