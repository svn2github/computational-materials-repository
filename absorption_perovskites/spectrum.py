# creates: spectrum.svg
"""Plot the absorption spectrum along the x direction for a given
perovskite"""

import matplotlib.pyplot as plt
import ase.db

# Connect to database:
c = ase.db.connect('absorption_perovskites.db')

# Select cubic symmetry containing Sn:
for n in c.select('name=AgNbO3'):
    name = n.name
    energy = n.data.energy
    im_eps_x = n.data.im_eps[0]
plt.plot(energy,im_eps_x)

plt.arrow(n.gllbsc_dir_gap, 2, 0.0, -1, fc="g", ec="g", head_width=0.2, head_length=0.3, head_starts_at_zero=False)

plt.text(n.gllbsc_dir_gap,2.1,'gap_d',rotation=90,horizontalalignment='center',verticalalignment='bottom',color='g')
if (n.gllbsc_dir_gap != n.gllbsc_ind_gap):
    plt.arrow(n.gllbsc_ind_gap, 2, 0.0, -1, fc="r", ec="r", head_width=0.2, head_length=0.3, head_starts_at_zero=False)
    plt.text(n.gllbsc_ind_gap,2.1,'gap_i',rotation=90,horizontalalignment='center',verticalalignment='bottom',color='r')

plt.ylabel('Abs. Spectrum [arb. units]')
plt.xlabel('Energy [eV]')
plt.text(7,0.5,name)
plt.savefig('spectrum.svg')
