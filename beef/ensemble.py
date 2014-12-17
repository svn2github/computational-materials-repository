from __future__ import print_function
import ase.db
from ase.dft.bee import BEEFEnsemble

c = ase.db.connect('beefgpaw.db')

def ensemble(name):
    d = c.get(formula=name, xc='mBEEF')
    bee = BEEFEnsemble(e=d.energy, contribs=d.data.contributions, xc='mBEEF')
    e = bee.get_ensemble_energies()
    return e
    
ae = 2 * ensemble('N') - ensemble('N2')
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
