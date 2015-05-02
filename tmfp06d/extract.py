import sys
import numpy as np
import ase.db
from ase.utils import prnt
from ase.data import chemical_symbols, atomic_numbers
from ase.structure import molecule
from ase.data.tmfp06d import data

molecule_names = sorted([m for m in data.keys() if len(molecule(m, data=data)) > 1])
atom_names = sorted([m for m in data.keys() if len(molecule(m, data=data)) == 1])

calc = sys.argv[1]
db = sys.argv[2]

c = ase.db.connect(db)

def analyse(calc, relaxed):
    e = {}
    for name in atom_names:
        try:
            d = c.get(name=name, natoms=1, calculator=calc)
            assert chemical_symbols[d.numbers[0]] == name
            e[d.numbers[0]] = d.energy
        except KeyError:
            e[atomic_numbers[name]] = np.nan
    
    A = []
    for name in molecule_names:
        try:
            d = c.get(name=name, relaxed=relaxed, calculator=calc)
            if np.nan in [e[Z] for Z in d.numbers] or np.isnan(d.energy):
                ea = np.nan
            else:
                ea = sum(e[Z] for Z in d.numbers) - d.energy
            dist = ((d.positions[0] - d.positions[-1])**2).sum()**0.5
            freq = d.frequency
            t = d.time
        except KeyError:
            ea = np.nan
            dist = np.nan
            freq = np.nan
            t = np.nan
        A.append((ea, dist, freq, t))
    return np.array(A).T


E0, D0, F0, T0 = analyse(calc, 0)
try:
    E1, D1, F1, T1 = analyse(calc, 1)
except KeyError:
    E1 = E0
    D1 = D0
    F1 = F0
    T1 = T0

fd = open('%s.csv' % db, 'w')
prnt('# Atomization energies (E), distances (d), frequencies (f) and time (t): %s %s' % (calc, db), file=fd)
prnt('# name (N), E(N; not relaxed), E(N), d(N), F(N; not relaxed), F(N),  t(N; not relaxed) [sec]', file=fd)
for name, e0, e1, d1, f0, f1, t0, in zip(molecule_names,
                                 E0, E1, D1, F0, F1, T0):
    prnt('%11s, %7.3f, %7.3f, %7.3f, %7.1f, %7.1f, %7.1f' %
         (name, e0, e1, d1, f0, f1, t0), file=fd)
