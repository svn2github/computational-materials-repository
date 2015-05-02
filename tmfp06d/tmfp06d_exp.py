import sys
import numpy as np
import ase.db
from ase.units import kcal, mol
from ase.utils import prnt
from ase.data import chemical_symbols, atomic_numbers
from ase.structure import molecule
from ase.data.tmfp06d import data

molecule_names = sorted([m for m in data.keys() if len(molecule(m, data=data)) > 1])
atom_names = sorted([m for m in data.keys() if len(molecule(m, data=data)) == 1])

db = 'tmfp06d_exp.db'

def analyse():
    A = []
    for name in molecule_names:
        try:
            ea = data[name].get('dissociation energy', np.nan) * kcal / mol
            dist = molecule(name, data=data).get_distance(0, 1)
            freq = data[name].get('harmonic frequency', np.nan)
            t = np.nan
        except KeyError:
            ea = np.nan
            dist = np.nan
            freq = np.nan
            t = np.nan
        A.append((ea, dist, freq, t))
    return np.array(A).T


E0, D0, F0, T0 = analyse()
try:
    E1, D1, F1, T1 = analyse()
except KeyError:
    E1 = E0
    D1 = D0
    F1 = F0
    T1 = T0

fd = open('%s.csv' % db, 'w')
prnt('# Atomization energies (E), distances (d), frequencies (f) and time (t): %s' % db, file=fd)
prnt('# name (N), E(N; not relaxed), E(N), d(N), F(N; not relaxed), F(N),  t(N; not relaxed) [sec]', file=fd)
for name, e0, e1, d1, f0, f1, t0, in zip(molecule_names,
                                 E0, E1, D1, F0, F1, T0):
    prnt('%11s, %7.3f, %7.3f, %7.3f, %7.1f, %7.1f, %7.1f' %
         (name, e0, e1, d1, f0, f1, t0), file=fd)
