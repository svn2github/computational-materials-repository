import os
import sys
import time

import numpy as np

import ase.db
from ase.units import Rydberg
from ase.utils import opencew
from ase.calculators.calculator import kpts2mp
from ase.io import Trajectory
from espresso import espresso as espressoORIG
from ase.test.tasks.gbrv import GBRVBulkCollection as Collection

# modifications needed to the old-style interfaces
class espresso(espressoORIG):
    name = 'espresso'
    def check_state(self, atoms): return []
    def todict(self): return {}

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

pw = 80
dw = 300

linspace = (0.98, 1.02, 5)  # eos numpy's linspace
if category == 'magnetic_moments':
    linspace = (1.0, 1.0, 1)  # eos numpy's linspace
linspacestr = ''.join([str(t) + 'x' for t in linspace])[:-1]

code = category + '_espresso' + '-' + '_p' + str(pw) + '_d' + str(dw) + '_e' + linspacestr
code = code + '_k' + str(kptdensity) + '_w' + str(width)

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
    if atoms.get_initial_magnetic_moments().any():  # spin-polarization
        kwargs.update({'spinpol': True})
    # loop over EOS linspace
    for n, x in enumerate(np.linspace(linspace[0], linspace[1], linspace[2])):
        id = c.reserve(category=category,
                       name=name, pw=pw, dw=dw,
                       linspacestr=linspacestr,
                       kptdensity=kptdensity, width=width,
                       x=x)
        if id is None:
            continue
        # perform EOS step
        atoms.set_cell(cell * x, scale_atoms=True)
        # set calculator
        atoms.calc = espresso(
            outdir=name + '_' + code + '_' + str(n),
            xc='PBE',
            kpts=kpts,
            kptshift=[(nk + 1) % 2 * 1 for nk in kpts],
            pw=pw*Rydberg,
            dw=dw*Rydberg,
            sigma=width,
            mode='scf',
            #'verbose':'high',
            #'noncollinear':True,
            #'spinorbit':True,
            output={'avoidio': True},  # will overwrite disk_io parameter if True
            convergence={'mixing': 0.2, 'maxsteps':200,},
        )
        atoms.calc.set(**kwargs)  # remaining calc keywords
        t = time.time()
        e = atoms.get_potential_energy()
        atoms.calc.results = {'energy': e}
        c.write(atoms,
                category=category,
                name=name, pw=pw, dw=dw,
                linspacestr=linspacestr,
                kptdensity=kptdensity, width=width,
                magnetic_moment=atoms.calc.get_magnetization()[0],
                x=x,
                time=time.time()-t)
        traj.write(atoms)
        del c[id]
