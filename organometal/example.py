# creates: example.svg
"""Plot the bandgaps as a function of the electronegativity
in the Mulliken's scale for a given crystal symmetry (cubic,
tetragonal, or orthorhombics)"""

import matplotlib.pyplot as plt
import ase.db
from ase.data import chemical_symbols


# Electronegativities:
xcl = 8.30
xbr = 7.59
xi = 6.76

# Connect to database:
c = ase.db.connect('organometal.db')

gaps = {'Cs': [], 'MA': [], 'FA': []}
electr = {'Cs': [], 'MA': [], 'FA': []}

# Select cubic symmetry containing Sn:
for row in c.select('Sn>=1', symmetry='cubic'):
    x = 1.0
    for Z in row.numbers:
        symbol = chemical_symbols[Z]
        if symbol == 'I':
            x *= xi
        elif symbol == 'Br':
            x *= xbr
        elif symbol == 'Cl':
            x *= xcl
    x = x**(1 / 3.0)

    name = row.name[:2]
    electr[name].append(x)
    gaps[name].append(row.gllbsc_ind_gap)

for name, symbol in zip(['Cs', 'MA', 'FA'], 'os*'):
    plt.plot(electr[name], gaps[name], symbol, label=name)

plt.ylabel('Bandgap [eV]')

X = ['I3', 'Br3', 'Cl3', 'I2Br', 'IBr2',
     'I2Cl', 'ICl2', 'IBrCl', 'Br2Cl', 'BrCl2']
chi = [xi**3, xbr**3, xcl**3, xi**2 * xbr, xi * xbr**2,
       xi**2 * xcl, xi * xcl**2, xi * xbr * xcl, xbr**2 * xcl, xbr * xcl**2]
chi = [x3**(1 / 3.0) for x3 in chi]

plt.xticks(chi, X, rotation=60)
plt.legend()
plt.savefig('example.svg')
