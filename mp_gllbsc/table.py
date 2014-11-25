"""Calculate errors in band gap relative to GW"""
from __future__ import print_function
import numpy as np
import ase.db

con = ase.db.connect('mp_gllbsc.db')

data = []
for dct in con.select('g0w0_gap'):
    ref = dct.gw_gap
    data.append([dct.gw0_gap - ref,
                 dct.g0w0_gap - ref,
                 dct.lda_gap - ref,
                 dct.gllbsc_gap - ref,
                 dct.gllbsc_gap - dct.gllbsc_disc - ref,
                 dct.hse06_gap - ref])
errors = np.array(data).T

labels = ['`GW_0`', '`G_0W_0`', 'LDA', 'GLLB-SC - `\Delta_{xc}`',
          'GLLB-SC - KS', 'HSE06']
f = open('gaps.csv', 'w')
print('Material, Mean error [eV], Mean absolute error [eV]', file=f)
for label, e in zip(labels, errors):
    print('{}, {:.2f}, {:.2f}'.format(label, e.mean(), abs(e).mean()), file=f)
