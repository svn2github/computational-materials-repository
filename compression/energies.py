import sys

import numpy as np

from ase.data import chemical_symbols
from ase.utils import prnt
import ase.db

names = chemical_symbols[1:103]
linspace = (0.700,0.800,0.850,0.900,0.925,0.950,0.975,1.000,1.025,1.050,1.075,1.100,1.125,1.150,1.175,1.200)

if len(sys.argv) == 2 and 'run.py' not in sys.argv:
    db = sys.argv[1]
else:
    db = 'compression.db'  # default db file

c = ase.db.connect(db)

def analyse(c, names, linspace):

    A = []
    for name in names:
        e = []  # energies
        for x in linspace:
            try:
                d = c.get(name=name, x=x)
                assert name == d.name
                e.append(d.energy)
            except (KeyError, AttributeError):
                e.append(np.nan)
        while len(e) < len(linspace):  # missing data
            e.append(np.nan)
        A.append(e)
    return A

E = analyse(c, names, linspace)

fd = open(db + '_energies.csv', 'w')
prnt('c' + ',' + ','.join([str(round(e, 3)) for e in linspace]), file=fd)
for name, energies, in zip(names, E):
    prnt(name + ',' + ','.join([str(round(e, 4)) for e in energies]), file=fd)
