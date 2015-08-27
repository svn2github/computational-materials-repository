import sys
import numpy as np
import ase.db
from ase.utils import prnt
from ase.data import chemical_symbols, atomic_numbers
from ase.structure import molecule
from ase.data.g2 import data
from ase.data.g2 import molecule_names

calc = sys.argv[1]
db = sys.argv[2]

c = ase.db.connect(db)

def analyse(calc, relaxed):
    A = []
    for name in molecule_names:
        # molecule
        ea = np.nan
        dist = np.nan
        t = np.nan
        formulas = [name]
        for i in range(len(molecule(name, data=data))):
            formulas.append(name + '_bq' + str(i))
        for formula in formulas:
            try:
                d = c.get(name=formula, relaxed=relaxed, calculator=calc)
                assert d.name == formula
                if 'bq' in formula:
                    print 'bq', d.name
                    ea = ea + d.energy
                else:
                    print 'molecule', d.name
                    ea = - d.energy
                dist = ((d.positions[0] - d.positions[-1])**2).sum()**0.5
                t = d.time
            except (KeyError, ValueError):
                ea = np.nan
                dist = np.nan
                t = np.nan
        A.append((ea, dist, t))
    return np.array(A).T


E0, D0, T0 = analyse(calc, 0)
try:
    E1, D1, T1 = analyse(calc, 1)
except KeyError:
    E1 = E0
    D1 = D0
    T1 = T0

fd = open('%s.csv' % db, 'w')
prnt('# Atomization energies (E), distances (d) and time (t): %s %s' % (calc, db), file=fd)
prnt('# name (N), E(N; not relaxed), E(N), d(N), t(N; not relaxed) [sec]', file=fd)
for name, e0, e1, d1, t0, in zip(molecule_names,
                                 E0, E1, D1, T0):
    prnt('%21s, %7.3f, %7.3f, %7.3f, %7.1f' %
         (name, e0, e1, d1, t0), file=fd)
