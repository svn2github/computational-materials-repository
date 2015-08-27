import os

import numpy as np
from numpy import nan
import csv

import matplotlib
matplotlib.use('Agg')

from matplotlib import pylab

from ase.data import atomic_numbers

# http://matplotlib.org/examples/pylab_examples/line_styles.html
linestyles = ['_', '-', '--', ':']
markers = []
for m in matplotlib.lines.Line2D.markers:
    try:
        if len(m) == 1 and m != ' ':
            markers.append(m)
    except TypeError:
        pass

styles = markers + [
    r'$\lambda$',
    r'$\bowtie$',
    r'$\circlearrowleft$',
    r'$\clubsuit$',
    r'$\checkmark$']

colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')

def CommentStripper(iterator):
    for line in iterator:
        if '#' in line:
            continue
        if 0:  # this kills minus!
            if '-' in line:
                continue
        if 'np' in line:
            continue
        if 'N/A' in line:
            continue
        if not line.strip():
            continue
        yield line

postfix = '.db'

files = [
    'aims_NAO-VCC-5Z.nrel' + postfix + '.csv',
    #'aims_NAO-VCC-5Z.srel' + postfix + '.csv',
    #'aims_aug-cc-pV5Z.nrel' + postfix + '.csv',
    #'aims_aug-cc-pV6Z.nrel' + postfix + '.csv',
    #'aims_aug-cc-pV6Z.srel' + postfix + '.csv',
    #'aims_aug-cc-pV5Z.srel' + postfix + '.csv',
    'nwchem_aug-cc-pv5z.bsse_corrected.nrel' + postfix + '.csv',
    'nwchem_aug-cc-pv5z.nrel' + postfix + '.csv',
    #'nwchem_def2-qzvppd.bsse_corrected.nrel' + postfix + '.csv',
    #'nwchem_def2-qzvppd.nrel' + postfix + '.csv',
    #'aims_tight.nrel' + postfix + '.csv',
    #'aims_tight.srel' + postfix + '.csv',
    #'aims_tier2.nrel' + postfix + '.csv',
    #'aims_tier2.srel' + postfix + '.csv',
    'aims_tier3.nrel' + postfix + '.csv',
    #'aims_tier3.srel' + postfix + '.csv',
    #'aims_aug-cc-pV5Z.nrel' + postfix + '.csv',
    #'aims_aug-cc-pV5Z.srel' + postfix + '.csv',  # strange results
    #'aims_aug-cc-pV6Z.nrel' + postfix + '.csv',
    #'aims_aug-cc-pV6Z.srel' + postfix + '.csv',
    #'espresso_sg15_oncv.srel' + postfix + '.csv',
    'gpaw_paw09.nrel' + postfix + '.csv',
    ]


data = []
for n, f in enumerate(files):
    reader = csv.reader(CommentStripper(open(f, 'r')), delimiter=',')
    d = []
    for r in reader:
        d.append([''.join(r1.split()) for r1 in r])
    data.append(d)


labels = [m[0] for m in data[0]]
scale = [l for l in range(len(labels))]
vm01 = [-0.1 for v in scale]
vm02 = [-0.2 for v in scale]
zero = [0.0 for v in scale]
v01 = [0.1 for v in scale]
v02 = [0.2 for v in scale]

pylab.plot(scale, zero, 'k-', label='_nolegend_')
pylab.plot(scale, vm01, 'k-', label='_nolegend_')
pylab.plot(scale, vm02, 'k-', label='_nolegend_')
pylab.plot(scale, v01, 'k-', label='_nolegend_')
pylab.plot(scale, v02, 'k-', label='_nolegend_')

pylab.gca().set_ylim(-0.3, 0.3)
pylab.gca().set_xlim(0, len(labels) - 1)

# http://matplotlib.org/examples/pylab_examples/axhspan_demo.html
for s in scale:
    l = pylab.axvline(x=s, linewidth=0.5, color=(0,0,0,0), alpha=0.5)

ay1 = pylab.gca()
ay1.xaxis.set_ticks([n for n in scale])
ay1.xaxis.set_ticklabels(labels)
if 0:
    ay1.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
ay1.yaxis.set_ticks([-0.2, -0.1, 0.0, 0.1, 0.2])
ay1.yaxis.set_ticklabels(['-0.2', '-0.1', '0.0', '0.1', '0.2'])

for label in ay1.get_xticklabels() + ay1.get_yticklabels():
    label.set_fontsize(6)
# rotate labels http://old.nabble.com/Rotate-x-axes-%28xticks%29-text.-td3141258.html
for n, label in enumerate(ay1.get_xticklabels()):
    label.set_rotation(85)
    label.set_position((0.0,1.0 * (n % 2)))


for n, f in enumerate(files[1:]):
    color = colors[n % len(colors)]
    name = os.path.splitext(os.path.basename(f))[0]
    name = name.replace('.db', '')
    name = name.replace('nwchem_aug-cc-pv5z.bsse_corrected.nrel', 'NWCHEM aug-cc-pv5z (qz for Li, Be, Na) non-relativistic BSSE corrected')
    name = name.replace('nwchem_aug-cc-pv5z.nrel', 'NWCHEM aug-cc-pv5z (qz for Li, Be, Na) non-relativistic')
    name = name.replace('nwchem_def2-qzvppd.bsse_corrected.nrel', 'NWCHEM def2-qzppd non-relativistic BSSE corrected')
    name = name.replace('nwchem_def2-qzvppd.nrel', 'NWCHEM def2-qzppd non-relativistic')
    name = name.replace('gpaw_paw09.nrel', 'GPAW PAW 0.9 non-relativistic')
    name = name.replace('gpaw_paw09.srel', 'GPAW PAW 0.9 scalar-relativistic')
    name = name.replace('espresso_sg15_oncv.srel', 'ESPRESSO NC SG15_ONCV scalar-relativistic')
    name = name.replace('aims_tight.nrel', 'FHI-AIMS tight non-relativistic')
    name = name.replace('aims_tight.srel', 'FHI-AIMS tight atomic_zora scalar')
    name = name.replace('aims_tier2.nrel', 'FHI-AIMS tier2 non-relativistic')
    name = name.replace('aims_tier2.srel', 'FHI-AIMS tier2 atomic_zora scalar')
    name = name.replace('aims_tier3.nrel', 'FHI-AIMS tier3 non-relativistic')
    name = name.replace('aims_tier3.srel', 'FHI-AIMS tier3 atomic_zora scalar')
    name = name.replace('aims_aug-cc-pV5Z.nrel', 'FHI-AIMS aug-cc-pV5Z non-relativistic')
    name = name.replace('aims_aug-cc-pV5Z.srel', 'FHI-AIMS aug-cc-pV5Z atomic_zora scalar')
    name = name.replace('aims_aug-cc-pV6Z.nrel', 'FHI-AIMS aug-cc-pV6Z non-relativistic')
    name = name.replace('aims_aug-cc-pV6Z.srel', 'FHI-AIMS aug-cc-pV6Z atomic_zora scalar')
    name = name.replace('aims_NAO-VCC-5Z.nrel', 'FHI-AIMS NAO-VCC-5Z non-relativistic')
    name = name.replace('aims_NAO-VCC-5Z.srel', 'FHI-AIMS NAO-VCC-5Z atomic_zora scalar')
    # column 1: atomization energy on G2 fixed strucures
    # column 2: atomization energy relaxed
    c = 1
    values = []
    for i, v in enumerate(data[n+1]):
        try:
            value = eval(v[c]) - eval(data[0][i][c])
        except IndexError:
            value = np.nan
        values.append(value)
    s = np.std([i for i in values if not np.isnan(i)])
    pylab.plot(scale, values, linestyle='-',
               marker=markers[n % len(markers)], color=color,
               label=name + ", stddev: %.2f" % s)

prop = matplotlib.font_manager.FontProperties(size=8)
leg = pylab.legend(loc='lower left', fancybox=True, prop=prop)
leg.get_frame().set_alpha(0.5)
# http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg03952.html
leg._loc=(0.01, 0.05)

t = pylab.title('PBE atomization energies of G2/97 molecules', fontsize=10)
# http://old.nabble.com/More-space-between-title-and-secondary-x-axis-td31722298.html
t.set_y(1.05)

pylab.xlabel('molecule')
pylab.ylabel('code - FHI-AIMS NAO-VCC-5Z non-relativistic [eV]')

pylab.savefig('g2.png', bbox_inches='tight', dpi=600)
