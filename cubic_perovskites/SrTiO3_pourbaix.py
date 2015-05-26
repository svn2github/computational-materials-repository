# creates: SrTiO3_pourbaix.png
import numpy as np
import ase.db
from ase.phasediagram import Pourbaix, solvated

con = ase.db.connect('cubic_perovskites.db')

refs = []
for row in con.select('reference'):
    refs.append((row.formula, row.standard_energy))

# Add other solid/dissolved phases not included before:
refs += [('Ti6O', -5.443), ('Ti2O3', -13.907), ('Ti2O', -5.164),
         ('TiO', -4.838), ('SrO2', -5.356), ('Ti3O', -5.346),
         ('Ti3O5', -22.917), ('Sr4Ti3O10', -50.756), ('SrTi11O20', -93.313)]

# Extract the dissolved phases:
refs += solvated('SrTi')

pb = Pourbaix(refs, Sr=1, Ti=1, O=3)
U = np.linspace(-2, 2, 200)
pH = np.linspace(-2, 15, 300)
d, names, text = pb.diagram(U, pH, plot=True, show=False)

import matplotlib.pyplot as plt
plt.savefig('SrTiO3_pourbaix.png')
