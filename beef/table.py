from __future__ import print_function
import ase.db
import numpy as np

cref = ase.db.connect('beef.db')
eref = np.array([d.ae for d in cref.select('natoms>1')])

c = ase.db.connect('beefgpaw.db')
xcs = [d.xc for d in c.select(name='H')]

data = []
for xc in xcs:
    energies = np.array([d.ae for d in c.select('natoms>1,xc=' + xc)])
    de = energies - eref
    data.append((xc, abs(de).mean(), de.min(), de.mean(), de.max()))
data.sort(key=lambda row: row[1])

fd = open('table.csv', 'w')
print('# XC,    MEANABS,     MIN,    MEAN,     MAX', file=fd)
for row in data:
    print('{:8}{:8.2f},{:8.2f},{:8.2f},{:8.2f}'.format(row[0] + ',', *row[1:]),
          file=fd)
