import os
import sys
import time

import numpy as np

import ase.db
from ase.units import Bohr, Hartree
from ase.utils import opencew
from ase.calculators.calculator import kpts2mp
from ase.io import Trajectory
from ase.calculators.exciting import Exciting as ExcitingORIG
# modifications needed to the old-style interfaces
class Exciting(ExcitingORIG):
    name = 'exciting'
    def check_state(self, atoms): return []
    def todict(self): return {}
from ase.test.tasks.gbrv import GBRVBulkCollection as Collection

# shift MP k-points
def get_vkloff(mp):
    vkloff = []  # is this below correct?
    for nk in mp:
        if nk % 2 == 0:  # shift kpoint away from gamma point
            vkloff.append(0.5)
        else:
            vkloff.append(0)
    return ','.join([str(v) for v in vkloff])

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

# medium used ~2.0 Bohr
preferred_rmt = 2.00

c = ase.db.connect('gbrv.db')

kptdensity = 16.0
width = 0.01

rgkmax = 8.5
gmaxvr = 25

lmaxapw = 10
lmaxvr = 7 # not important
lmaxmat = 10

linspace = (0.98, 1.02, 5)  # eos numpy's linspace
linspacestr = ''.join([str(t) + 'x' for t in linspace])[:-1]

# find minimal distances in bcc
rmt_max = {}
C = Collection(category='bcc')
for name in C.names:
    d = 100.0
    A = C[name].repeat((2,2,2))
    for n1 in range(len(A)):
        for n2 in range(len(A)):
            if n1 != n2 and A.get_distance(n1, n2) < d:
                d = A.get_distance(n1, n2)
    if d < 100.0:
        # atomic radius * 0.98 - 0.03 Bohr
        # ase.io.exciting converts Angstrom -> Bohr
        rmt_max[name] = min(preferred_rmt, round(d * linspace[0] / 2 / Bohr - 0.03, 2)) * Bohr

# some default rmt
rmt_orig = {
    'H': 1.1 * Bohr,
    'He': 1.2 * Bohr,
    'Ne': 1.2 * Bohr,
    'Be': 1.45 * Bohr,
    'B': 1.45 * Bohr,
    'C': 1.45 * Bohr,
    'N': 1.45 * Bohr,
    'O': 1.45 * Bohr,
    'F': 1.25 * Bohr,  # 1.45 default
    'S': 1.45 * Bohr,
    'Cl': 1.45 * Bohr,
    'Ar': 1.45 * Bohr,
    'Li': 1.7 * Bohr,
    #
    'Mg': 1.8 * Bohr,
    'K': 2.4 * Bohr,
    'Ca': 2.2 * Bohr,
    'As': 2.2 * Bohr,
    'Rb': 2.4 * Bohr,
    'Cs': 2.2 * Bohr,
    'Hf': 2.2 * Bohr,
    'Pt': 2.1 * Bohr,
    'Hg': 1.8 * Bohr,
    }

# decrease rmt_orig to rmt_max (only if needed)
rmt = {}
for name in C.names:
    if name not in rmt_orig:
        rmt[name] = rmt_max[name]
    else:
        rmt[name] = rmt_orig[name]

code = category + '_exciting' + '-' + 'r' + str(rgkmax) + '_g' + str(gmaxvr) + '_e' + linspacestr
code = code + '_k' + str(kptdensity) + '_w' + str(width)
code = code + '_l' + str(lmaxapw) + str(lmaxvr) + str(lmaxmat)
#code = code + '_f' + str(fracinr)
code = code + '_r' + str(preferred_rmt)

names = names

for name in names:
    # save all steps in one traj file in addition to the database
    # we should only used the database c.reserve, but here
    # traj file is used as another lock ...
    fd = opencew(name + '_' + code + '.traj')
    if fd is None:
        continue
    traj = Trajectory(name + '_' + code + '.traj', 'w')
    atoms = collection[name]
    # create atoms.rmt array to fix rmt
    a = []
    for n, s in enumerate(atoms.get_chemical_symbols()):
        a.append(rmt[s])
    atoms.set_array('rmt', a, float, ())
    cell = atoms.get_cell()
    kpts = tuple(kpts2mp(atoms, kptdensity, even=True))
    kwargs = {
        'xctype':'GGA_PBE',
        'kpts':kpts,
        'swidth':width / Hartree,
        'rgkmax':rgkmax,
        'gmaxvr':gmaxvr,
        'maxscl':600,
        # http://sourceforge.net/projects/elk/forums/forum/897820/topic/5089864
        # http://sourceforge.net/projects/elk/forums/forum/897820/topic/5074106
        'lmaxapw':lmaxapw, # default 8
        'lmaxvr':lmaxvr, # default 7
        'lmaxmat':lmaxmat, # very important # default 5
        'do':'fromscratch',
        #'solscf':1000,
        #'fracinr':1.e-12,
        'SymmetricKineticEnergy':'true',
        'ValenceRelativity':'iora*',
        'useDM':'true',
        }
    kwargs.update({'vkloff': get_vkloff(kpts)})  # k-points shift
    kwargs.update({'speciespath': os.path.join(os.environ['EXCITING_SPECIES_PATH'])})
    kwargs.update({'bin': 'mpiexec ' + os.path.join(os.environ['EXCITINGROOT'], 'bin/excitingmpi')})
    kwargs.update({'autormt': False})
    # loop over EOS linspace
    for n, x in enumerate(np.linspace(linspace[0], linspace[1], linspace[2])):
        id = c.reserve(category=category,
                       name=name, rgkmax=rgkmax, gmaxvr=gmaxvr, linspacestr=linspacestr,
                       kptdensity=kptdensity, width=width,
                       lmaxapw=lmaxapw, lmaxvr=lmaxvr, lmaxmat=lmaxmat,
                       preferred_rmt=str(preferred_rmt),
                       x=x)
        if id is None:
            continue
        label=name + '_' + code + '_' + str(n)
        # perform EOS step
        atoms.set_cell(cell * x, scale_atoms=True)
        kwargs.update({'dir': label})
        # set calculator
        atoms.calc = Exciting(**kwargs)
        t = time.time()
        e = atoms.get_potential_energy()
        atoms.calc.results = {'energy': e}
        c.write(atoms,
                category=category,
                name=name, rgkmax=rgkmax, gmaxvr=gmaxvr, linspacestr=linspacestr,
                kptdensity=kptdensity, width=width,
                lmaxapw=lmaxapw, lmaxvr=lmaxvr, lmaxmat=lmaxmat,
                preferred_rmt=str(preferred_rmt),
                x=x,
                time=time.time()-t)
        traj.write(atoms)
        for wfk in [
            os.path.join(label, 'EVECFV.OUT'),
            os.path.join(label, 'EVECSV.OUT'),
            os.path.join(label, 'STATE.OUT'),
            ]:
            if os.path.exists(wfk): os.remove(wfk)
        del c[id]
