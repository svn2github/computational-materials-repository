import sys
import numpy as np
from numpy.linalg.linalg import LinAlgError
from ase.units import kJ
import ase.db
from ase.utils import prnt
from ase.atoms import string2symbols
from ase.data import chemical_symbols
from ase.test.tasks.gbrv import GBRVBulkCollection as Collection
from ase.test.tasks.dcdft import FullEquationOfState as EquationOfState

if len(sys.argv) == 2 and 'run.py' not in sys.argv:
    db = sys.argv[1]
    category = 'fcc'
elif len(sys.argv) == 3 and 'run.py' not in sys.argv:
    db = sys.argv[1]
    category = sys.argv[2]
else:
    db = 'gbrv.db'  # default db file
    category = 'fcc'

collection = Collection(category=category)

category_ref = 'fcc'  # reference for calculating formation energies
assert category_ref in ['fcc', 'bcc']

c = ase.db.connect(db)

def analyse(c, collection, category, category_ref=None):

    A = []
    for name in collection.names:
        ve = []  # volume, energy pairs
        for d in c.select(category=category, name=name):
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
            (v, e0, B0, B1, R) = (np.nan, np.nan, np.nan, np.nan, np.nan)
        if not R: R = [np.nan]  # sometimes R is an empty array
        if not isinstance(R, list): R = [R]  # sometimes R is not a list
        e = e0  # formation energy
        # number of unit formulas per cell
        nufpc = len(collection[name]) / len(string2symbols(name))
        # calculate formation energy wrt category_ref
        if category_ref:
            for d in c.select(category=category, name=name, x=1.000):
                for n in d.numbers:
                    # use gbrv structure (x=1.000)
                    for d1 in c.select(category=category_ref, name=chemical_symbols[n], x=1.000):
                        assert len(set(d1.numbers)) == 1
                        e = e - d1.energy / len(d1.numbers)
        e0 = e0 / nufpc
        e = e / nufpc
        v = v / nufpc
        B0 = B0 / kJ * 1.0e24  # GPa
        A.append((e, e0, v, B0, B1, R[0]))
    return np.array(A).T

E, E0, V, B0, B1, R = analyse(c, collection, category, category_ref)

fd = open(db + '_' + category + '_raw.txt', 'w')
for name, e, e0, v, b0, b1, r, in zip(collection.names, E, E0, V, B0, B1, R):
    if not np.isnan(e):
        prnt('%2s %7.3f %8.4f %8.4f %8.4f %8.4f' % (name, e, e0, v, b0, b1), file=fd)
fd = open(db + '_' + category + '_raw.csv', 'w')
for name, e, e0, v, b0, b1, r, in zip(collection.names, E, E0, V, B0, B1, R):
    if not np.isnan(e):
        prnt('%s, %7.3f, %8.4f, %8.4f, %8.4f, %8.4f' % (name, e, e0, v, b0, b1), file=fd)
