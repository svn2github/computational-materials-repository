from sys import argv
import pickle
import numpy as np
from ase.db import connect

# Extract data and save to .pckl file
c = connect('vdWH_BuildingBlocks.db')
names = ['H-MoS2']
for name in names:
    d = c.get(name=name)
    pickle.dump((np.array(d.data.q),
                 np.array(d.data.frequencies),
                 np.array(d.data.chi_monopole),
                 np.array(d.data.chi_dipole),
                 np.array(d.data.z),
                 np.array(d.data.drho_monopole),
                 np.array(d.data.drho_dipole)), 
                open('%s-chi.pckl'%name, 'w'))

# Calculate static dielectric function for multilayer MoS2
# for 1 to 20 layers

from QEH import Heterostructure
import pylab as p
for n in [1,2,3,4,5,10,20]:
    d = [6.15 for i in range(n-1)]
    HS = Heterostructure(structure = ['%dH-MoS2'%n],  # set up structure
                         d=d,                         # layer distance array
                         include_dipole=True,         
                         wmax=0,                      # only include w=0
                         qmax=1,                      # q grid up to 1 Ang^{-1}
                         d0 = 6.15)                   # width of single layer
    q, epsM = HS.get_macroscopic_dielectric_function()
    p.plot(q, epsM, label=' N = %s'%n)

p.xlim(0,1)
p.xlabel('$q_\parallel (\mathrm{\AA^{-1}}$)', fontsize= 20)
p.ylabel('$\epsilon_M(q, \omega=0)$', fontsize= 20)
p.title('Static dielectric function', fontsize= 20)
p.legend(ncol=2, loc = 'best')
p.subplots_adjust(bottom=0.12)
p.savefig('epsMoS2.png')
p.show()
