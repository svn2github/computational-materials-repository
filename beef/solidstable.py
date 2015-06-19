# creates: lp.csv, ce.csv, bm.csv
from __future__ import print_function, division
import operator
import ase.db
import numpy as np

con = ase.db.connect('solids.db')

xcs = [row.xc for row in con.select(name='FeAl', calculator='gpaw')]

for key in ['lp', 'ce', 'bm']:
    fd = open(key + '.csv', 'w')
    if key == 'lp':
        key = 'volume'
    refs = {row.name: row.get(key) for row in
            con.select(calculator='exp')}
        
    data = []
    for xc in xcs:
        errors = []
        for row in con.select(xc=xc, pbc='TTT'):
            value = row.get(key)
            ref = refs.get(row.name)
            if value is not None and ref is not None:
                if key == 'volume':
                    errors.append(100 * (value / ref)**(1 / 3) - 100)
                else:
                    errors.append(value - ref)
        errors = np.array(errors)
        data.append((xc, len(errors), abs(errors).mean(),
                     errors.min(), errors.mean(), errors.max()))
    
    data.sort(key=operator.itemgetter(2))

    print('# XC, NUMBER, MEANABS, MIN, MEAN, MAX', file=fd)
    for row in data:
        print('{},{},{:.3f},{:.3f},{:.3f},{:.3f}'.format(*row), file=fd)
    fd.close()
