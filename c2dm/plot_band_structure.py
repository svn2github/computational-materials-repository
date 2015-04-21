# creates: H-MoS2_band_structure.png
from math import floor, ceil
import matplotlib.pyplot as plt
import ase.db

name = 'MoS2'
phase = 'H'

txtname = phase + '-' + name.replace('2', '$_2$')

# Connect to database
db = ase.db.connect('c2dm.db')
# Get the db row
row = db.get(name=name, phase=phase, xc='LDA')

ef = row.data['efermi'] # Fermi level
x_k = row.data['xbs_k'] # LDA band structure coordinates
e_kn = row.data['ebs_kn'] # LDA band structure energies

xqp_k = row.data['xqpbs_k'] # GW band structure coordinates
eqp_kn = row.data['qpbs_kn'] # GW band structure energies

x_K = row.data['xbs_K'] # Coordinates of high symmetry points
labels_K = row.data['bslabels_K'] # Names of high symmetry points
# Use Gamma symbol instead of 'Gamma'
for K, label in enumerate(labels_K):
    if label == 'Gamma':
        labels_K[K] = r'$\Gamma$'

ppi = 100
figw = 600 # Width in pixels
figh = 400 # Height in pixels
plt.figure(figsize=(figw / ppi, figh / ppi), dpi=ppi)
ldaplot = plt.plot(x_k, e_kn, '-k')
gwplot = plt.plot(xqp_k, eqp_kn, 'o-r')
plt.axhline(ef, linestyle='--', color='black')
plt.annotate('$E_\mathrm{f}$', xy=(0.05 * x_k[-1], ef),
             xytext=(0.05 * x_k[-1], ef + 0.25))
plt.legend([ldaplot[0], gwplot[0]], ['LDA', '$G_0W_0$'])
plt.ylim(floor(ef) - 5, ceil(ef) + 5)
plt.xlim(0, x_k[-1])
plt.xticks(x_K, labels_K)
plt.ylabel('Energy (eV)')
plt.title('Band structure of %s' % txtname)
plt.tight_layout()
plt.savefig('%s-%s_band_structure.png' % (phase, name))

