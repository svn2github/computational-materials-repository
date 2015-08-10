# Purpose: this script can extract the DOI volumes for e.g. VASP
# if in GBRVBulkCollection, .index('fcc') is replaced by .index('aVASP'), etc.

import sys

import numpy as np

from ase.utils import prnt
from ase.atoms import string2symbols
from ase.test.tasks.gbrv import GBRVBulkCollection as Collection

collection = Collection()

if len(sys.argv) == 1:
    category = 'fcc'
    collection = Collection()
    names = collection.names
elif len(sys.argv) == 2:
    category = sys.argv[1]
    collection = Collection(category=category) 
    names = collection.names
else:
    category = sys.argv[1]
    collection = Collection(category=category) 
    names = [sys.argv[2]]

fd = open('doi_' + category + '_raw.csv', 'w')

for name in names:
    e = 0.0
    e0 = 0.0
    b0 = 0.0
    b1 = 0.0
    if name in ['N', 'Hg']:
        e = np.nan
    # number of unit formulas per cell
    nufpc = len(collection[name]) / len(string2symbols(name))
    v = collection[name].get_volume()
    v = v / nufpc
    if not np.isnan(e):
        prnt('%s, %7.3f, %8.4f, %8.4f, %8.4f, %8.4f' % (name, e, e0, v, b0, b1), file=fd)
