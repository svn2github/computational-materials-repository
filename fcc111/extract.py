import sys
import csv
import numpy as np
from numpy import nan
import ase.db
from ase.utils import prnt
from ase.atoms import string2symbols
from ase.data import chemical_symbols

if len(sys.argv) == 2 and 'run.py' not in sys.argv:
    db = sys.argv[1]
else:
    db = 'fcc111.db'  # default db file

c = ase.db.connect(db)

names = chemical_symbols[1:103]

def analyse(c, names):

    A = []
    for name in names:
        # surface, surfaceO, surfaceC, bulkO, bulkC, distanceO, distanceC, sitier, stime
        results = [nan] * 9
        try:
            results[0] = c.get(name=name, category='fcc111', adsorbate='').energy
            results[1] = c.get(name=name, category='fcc111', adsorbate='O').energy
            results[2] = c.get(name=name, category='fcc111', adsorbate='C').energy
            results[3] = c.get(name='O', category='fcc', adsorbate='').energy
            results[4] = c.get(name='C', category='fcc', adsorbate='').energy
            results[5] = c.get(name=name, category='fcc111', adsorbate='O').toatoms().get_distance(12, 16)
            results[6] = c.get(name=name, category='fcc111', adsorbate='C').toatoms().get_distance(12, 16)
            # optional
            siter = 0  # sum of all SCF iterations
            stime = 0  # total time
            N = 0
            siter = siter + c.get(name=name, category='fcc111', adsorbate='').niter
            stime = stime + c.get(name=name, category='fcc111', adsorbate='').time
            N = N + 1
            siter = siter + c.get(name=name, category='fcc111', adsorbate='O').niter
            stime = stime + c.get(name=name, category='fcc111', adsorbate='O').time
            N = N + 1
            siter = siter + c.get(name=name, category='fcc111', adsorbate='C').niter
            stime = stime + c.get(name=name, category='fcc111', adsorbate='C').time
            N = N + 1
            siter = siter + c.get(name='O', category='fcc', adsorbate='').niter
            stime = stime + c.get(name='O', category='fcc', adsorbate='').time
            N = N + 1
            siter = siter + c.get(name='C', category='fcc', adsorbate='').niter
            stime = stime + c.get(name='C', category='fcc', adsorbate='').time
            N = N + 1
            results[7] = siter / N
            results[8] = stime / N
        except:
            pass
        A.append(results)
    return np.array(A)

results = analyse(c, names)

fd = open(db + '_raw.txt', 'w')
for name, r in zip(names, results):
    prnt('%2s %s' % (name, str(' '.join([str(round(r0, 4)) for r0 in r]))), file=fd)
fd = open(db + '_raw.csv', 'w')
for name, r in zip(names, results):
    prnt('%2s,%s' % (name, str(','.join([str(round(r0, 4)) for r0 in r]))), file=fd)
