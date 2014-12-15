from __future__ import print_function
import ase.db
from ase.dft.bee import BEEFEnsemble

c = ase.db.connect('beefgpaw.db')


def ensemble(name):
    d = c.get(formula=name, xc='mBEEF')
    bee = BEEFEnsemble(e=0, contribs=d.data.contributions, xc='mBEEF')
    e = bee.get_ensemble_energies() + d.energy
    return e
    
ae = 2 * ensemble('N') - ensemble('N2')
print('AE =', ae.mean(), '+-', ae.std())
print('AE =', ae.mean(), '+-', ae.std(), file=open('output.txt', 'w'))

import matplotlib.pyplot as plt
plt.hist(ae)
plt.savefig('hist.svg')
