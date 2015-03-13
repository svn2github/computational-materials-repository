# creates: epsMoS2.svg
import pickle
from ase.db import connect

# Extract data and save to .pckl files:
c = connect('c2dm.db')
names = ['H-MoS2']
for name in names:
    d = c.get(name=name)
    pickle.dump((d.data.q,
                 d.data.frequencies,
                 d.data.chi_monopole,
                 d.data.chi_dipole,
                 d.data.z,
                 d.data.drho_monopole,
                 d.data.drho_dipole),
                open('%s-chi.pckl' % name, 'w'),
                pickle.HIGHEST_PROTOCOL)

# Calculate static dielectric function for multilayer MoS2 for 1 to 20 layers:
from qeh import Heterostructure
import matplotlib.pyplot as plt
for n in [1, 2, 3, 4, 5, 10, 20]:
    d = [6.15 for i in range(n - 1)]
    HS = Heterostructure(structure=['%dH-MoS2' % n],  # set up structure
                         d=d,                         # layer distance array
                         include_dipole=True,
                         wmax=0,                      # only include w=0
                         qmax=1,                      # q grid up to 1 Ang^{-1}
                         d0=6.15)                     # width of single layer
    q, epsM = HS.get_macroscopic_dielectric_function()
    plt.plot(q, epsM, label=' N = %s' % n)

plt.xlim(0, 1)
plt.xlabel('$q_\parallel (\mathrm{\AA^{-1}}$)', fontsize=20)
plt.ylabel('$\epsilon_M(q, \omega=0)$', fontsize=20)
plt.title('Static dielectric function', fontsize=20)
plt.legend(ncol=2, loc='best')
plt.subplots_adjust(bottom=0.12)
plt.savefig('epsMoS2.svg')
