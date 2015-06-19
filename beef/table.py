# creates: table.csv
from __future__ import print_function
import operator
import ase.db
import numpy as np

con = ase.db.connect('molecules.db')
eref = [row.ae for row in
        con.select(calculator='exp', sort='name')]
eref = np.array(eref)

xcs = [row.xc for row in con.select(name='H', calculator='gpaw')]

data = []
for xc in xcs:
    energies = [row.ae for row in
                con.select('natoms>1', xc=xc, sort='name')]
    de = energies - eref
    data.append((xc, abs(de).mean(), de.min(), de.mean(), de.max()))
    
data.sort(key=operator.itemgetter(1))

fd = open('table.csv', 'w')
print('# XC,    MEANABS,     MIN,    MEAN,     MAX', file=fd)
for row in data:
    print('{:8}{:8.2f},{:8.2f},{:8.2f},{:8.2f}'.format(row[0] + ',', *row[1:]),
          file=fd)
