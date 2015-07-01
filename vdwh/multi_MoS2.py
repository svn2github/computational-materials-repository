# creates: epsMoS2.svg
import os
import sys
sys.path.insert(0, '.')
os.system('tar xf chi-data.tar.gz; mv chi-data/H-MoS2-chi.pckl .')
os.system('wget https://trac.fysik.dtu.dk/projects/gpaw/browser/trunk'
          '/gpaw/response/qeh.py?format=txt -O qeh.py')

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
