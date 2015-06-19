# creates: output.txt, hist.svg
from __future__ import print_function
import ase.db
from ase.dft.bee import ensemble

con = ase.db.connect('molecules.db')


row1 = con.get(formula='N', xc='mBEEF')
e1 = ensemble(row1.energy, row1.data.contributions, 'mBEEF')
row2 = con.get(formula='N2', xc='mBEEF')
e2 = ensemble(row2.energy, row2.data.contributions, 'mBEEF')
ae = 2 * e1 - e2

print('AE = {0:.2f} +- {1:.2f} eV'.format(ae.mean(), ae.std()))
# One more time to output.txt:
print('AE = {0:.2f} +- {1:.2f} eV'.format(ae.mean(), ae.std()),
      file=open('output.txt', 'w'))

assert abs(ae.mean() - 9.692) < 0.01
assert abs(ae.std() - 0.369) < 0.01

import matplotlib.pyplot as plt
plt.hist(ae, bins=20, normed=True, alpha=0.5)
plt.xlabel('atomization energy [eV]')
plt.ylabel('probability')
plt.savefig('hist.svg')
