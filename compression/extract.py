from __future__ import print_function

import sys
import numpy as np
from numpy import nan
from numpy.linalg.linalg import LinAlgError
from ase.units import kJ
from ase.data import chemical_symbols
import ase.db
from ase.utils import prnt
from ase.test.tasks.dcdft import FullEquationOfState as EquationOfState

names = chemical_symbols[1:103]

if len(sys.argv) == 2 and 'run.py' not in sys.argv:
    db = sys.argv[1]
else:
    db = 'compression.db'  # default db file

c = ase.db.connect(db)

def analyse(c, names):

    A = []
    for name in names:
        ve = []  # volume, energy pairs
        for d in c.select(name=name):
            try:
                assert name == d.name
                ve.append((abs(np.linalg.det(d.cell)), d.energy))
            except AttributeError:
                ve.append((np.nan, np.nan))

        # sort according to volume
        ves = sorted(ve, key=lambda x: x[0])

        # EOS
        eos = EquationOfState([t[0] for t in ves],
                              [t[1] for t in ves])
        try:
            v, e0, B0, B1, R = eos.fit()
        except (ValueError, TypeError, LinAlgError):
            (v, e0, B0, B1, R) = (np.nan, np.nan, np.nan, np.nan, [np.nan])
        if not R: R = [np.nan]  # sometimes R is an empty array
        e0 = e0
        v = v
        B0 = B0 / kJ * 1.0e24  # GPa
        A.append((e0, v, B0, B1, R[0]))
    return np.array(A).T

E0, V, B0, B1, R = analyse(c, names)

fd = open(db + '_raw.txt', 'w')
for name, e0, v, b0, b1, r, in zip(names, E0, V, B0, B1, R):
    if not np.isnan(e0):
        prnt('%2s %8.4f %8.4f %8.4f %8.4f' % (name, e0, v, b0, b1), file=fd)
fd = open(db + '_raw.csv', 'w')
for name, e0, v, b0, b1, r, in zip(names, E0, V, B0, B1, R):
    if not np.isnan(e0):
        prnt('%s, %8.4f, %8.4f, %8.4f, %8.4f' % (name, e0, v, b0, b1), file=fd)
