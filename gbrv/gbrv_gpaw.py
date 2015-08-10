import os
import sys
import time

import numpy as np

import ase.db
from ase.units import Rydberg
from ase.utils import opencew
from ase.calculators.calculator import kpts2mp
from ase.io import Trajectory
from gpaw import GPAW, PW
from gpaw.mixer import Mixer
from gpaw.utilities import h2gpts
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

kptdensity = 12.0
width = 0.01

mode = 'fd'
mode = 'pw'

e = 0.10  # h -> gpts
e = round(80 * Rydberg, 0)

relativistic = True
constant_basis = True  # preferred

if relativistic:
    linspace = (0.98, 1.02, 5)  # eos numpy's linspace
else:
    linspace = (0.92, 1.08, 7)  # eos numpy's linspace
if category == 'magnetic_moments':
    linspace = (1.0, 1.0, 1)  # eos numpy's linspace
linspacestr = ''.join([str(t) + 'x' for t in linspace])[:-1]

code = category + '_gpaw' + '-' + mode + str(e) + '_c' + str(constant_basis)
code = code + '_e' + linspacestr
code = code + '_k' + str(kptdensity) + '_w' + str(width)
code = code + '_r' + str(relativistic)

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
    if mode == 'fd':
        if constant_basis:
            # gives more smooth EOS in fd mode
            kwargs.update({'gpts': h2gpts(e, cell)})
        else:
            kwargs.update({'h': e})
    elif mode == 'pw':
        if constant_basis:
            kwargs.update({'mode': PW(e, cell=cell)})
        else:
            kwargs.update({'mode': PW(e)})
    if name in ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Ca', 'Sr', 'Ba']:
        # results wrong / scf slow with minimal basis
        kwargs.update({'basis': 'dzp'})
        kwargs.update({'nbands': -5})
    # loop over EOS linspace
    for n, x in enumerate(np.linspace(linspace[0], linspace[1], linspace[2])):
        id = c.reserve(category=category,
                       name=name, e=e, linspacestr=linspacestr,
                       kptdensity=kptdensity, width=width,
                       relativistic=relativistic,
                       constant_basis=constant_basis,
                       x=x)
        if id is None:
            continue
        # perform EOS step
        atoms.set_cell(cell * x, scale_atoms=True)
        # set calculator
        atoms.calc = GPAW(
            txt=name + '_' + code + '_' + str(n) + '.txt',
            xc='PBE',
            kpts=kpts,
            width=width,
            parallel={'band': 1},
            idiotproof=False)
        atoms.calc.set(**kwargs)  # remaining calc keywords
        t = time.time()
        atoms.get_potential_energy()
        c.write(atoms,
                category=category,
                name=name, e=e, linspacestr=linspacestr,
                kptdensity=kptdensity, width=width,
                relativistic=relativistic,
                constant_basis=constant_basis,
                x=x,
                magnetic_moment=atoms.calc.get_magnetic_moment(),
                niter=atoms.calc.get_number_of_iterations(),
                time=time.time()-t)
        traj.write(atoms)
        del c[id]
