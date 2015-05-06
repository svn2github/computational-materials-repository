# creates: gaps.csv
"""Calculate errors in band gap relative to GW"""
from __future__ import print_function
import numpy as np
import ase.db

con = ase.db.connect('mp_gllbsc.db')

data = []
for row in con.select('g0w0_gap'):
    ref = row.gw_gap
    data.append([row.gw0_gap - ref,
                 row.g0w0_gap - ref,
                 row.lda_gap - ref,
                 row.gllbsc_gap - ref,
                 row.gllbsc_gap - row.gllbsc_disc - ref,
                 row.hse06_gap - ref])
errors = np.array(data).T

labels = ['`GW_0`', '`G_0W_0`', 'LDA', 'GLLB-SC - `\Delta_{xc}`',
          'GLLB-SC - KS', 'HSE06']
f = open('gaps.csv', 'w')
print('Material, Mean error [eV], Mean absolute error [eV]', file=f)
for label, e in zip(labels, errors):
    print('{}, {:.2f}, {:.2f}'.format(label, e.mean(), abs(e).mean()), file=f)
