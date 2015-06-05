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

markers = ['D', 's', '|', 'x', '_', '^', 'd', 'h', '+', '*', ',', 'o', '.', '1', 'p', '3', '2', '4', 'H', 'v', '8', '<', '>']
markers = ['D', 's', '^', 'd', 'h', '+', '*', ',', 'o', '.', '1', 'p', '3', '2', '4', 'H', 'v', '8', '<', '>']

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
        if line.startswith('c'):
            continue
        if line.startswith('e'):
            continue
        if 'N/A' in line:
            continue
        if not line.strip():
            continue
        yield line

relativistic = 'srel'
relativistic = 'nrel'
#structure = 'rocksalt.'
structure = 'fcc.'
postfix = '.remove.db_energies'
#postfix = '.db_energies'

files = [
    structure + 'aims_tier2.' + relativistic + postfix + '.csv',
    structure + 'elk.' + relativistic + postfix + '.csv',
    structure + 'exciting.' + relativistic + postfix + '.csv',
    #structure + 'exciting.zora' + postfix + '.csv',
    #structure + 'exciting.iora*' + postfix + '.csv',
    #structure + 'espresso_gbrv_1.4.' + relativistic + postfix + '.csv',
    #structure + 'espresso_sg15_oncv.' + relativistic + postfix + '.csv',
    #structure + 'espresso_sssp_accurate.' + relativistic + postfix + '.csv',
    #structure + 'vaspsc.' + relativistic + postfix + '.csv',
    structure + 'gpaw_paw09.' + relativistic + postfix + '.csv',
    ]


data = []
for n, f in enumerate(files):
    reader = csv.reader(CommentStripper(open(f, 'r')), delimiter=',')
    d = []
    for r in reader:
        d.append([''.join(r1.split()) for r1 in r])
    data.append(d)


labels = [l[0] for l in data[0]]
scale = [atomic_numbers[l] for l in labels]
zero = [0.0 for v in scale]
v01 = [0.1 for v in scale]
v02 = [0.2 for v in scale]
v04 = [0.4 for v in scale]
v05 = [0.5 for v in scale]
v06 = [0.6 for v in scale]
v07 = [0.7 for v in scale]
v08 = [0.8 for v in scale]
v09 = [0.9 for v in scale]
v10 = [1.0 for v in scale]
v11 = [1.1 for v in scale]
v12 = [1.2 for v in scale]
v13 = [1.3 for v in scale]
v14 = [1.4 for v in scale]
v15 = [1.5 for v in scale]
v16 = [1.6 for v in scale]
v17 = [1.7 for v in scale]
v18 = [1.8 for v in scale]
v19 = [1.9 for v in scale]
v20 = [2.0 for v in scale]
v21 = [2.1 for v in scale]
v22 = [2.2 for v in scale]
v23 = [2.3 for v in scale]
vm01 = [-0.1 for v in scale]
vm02 = [-0.2 for v in scale]
vm03 = [-0.3 for v in scale]
vm04 = [-0.4 for v in scale]
vm05 = [-0.5 for v in scale]

pylab.plot(scale, vm05, 'k-', label='_nolegend_')
pylab.plot(scale, vm02, 'k-', label='_nolegend_')
pylab.plot(scale, vm01, 'k-', label='_nolegend_')
pylab.plot(scale, zero, 'k-', label='_nolegend_')
pylab.plot(scale, v01, 'k-', label='_nolegend_')
pylab.plot(scale, v02, 'k-', label='_nolegend_')
#pylab.plot(scale, v035, 'k-', label='_nolegend_')
pylab.plot(scale, v05, 'k-', label='_nolegend_')
#pylab.plot(scale, v06, 'k-', label='_nolegend_')
#pylab.plot(scale, v07, 'k-', label='_nolegend_')
#pylab.plot(scale, v08, 'k-', label='_nolegend_')
#pylab.plot(scale, v09, 'k-', label='_nolegend_')
#pylab.plot(scale, v10, 'k-', label='_nolegend_')
#pylab.plot(scale, v11, 'k-', label='_nolegend_')
#pylab.plot(scale, v12, 'k-', label='_nolegend_')
pylab.plot(scale, v13, 'k-', label='_nolegend_')
#pylab.plot(scale, v14, 'k-', label='_nolegend_')
#pylab.plot(scale, v15, 'k-', label='_nolegend_')
pylab.plot(scale, v16, 'k-', label='_nolegend_')
pylab.plot(scale, v17, 'k-', label='_nolegend_')
pylab.plot(scale, v18, 'k-', label='_nolegend_')
pylab.plot(scale, v19, 'k-', label='_nolegend_')
pylab.plot(scale, v20, 'k-', label='_nolegend_')
#pylab.plot(scale, v21, 'k-', label='_nolegend_')
#pylab.plot(scale, v22, 'k-', label='_nolegend_')
pylab.plot(scale, v23, 'k-', label='_nolegend_')
#pylab.plot(scale, v24, 'k-', label='_nolegend_')
#pylab.plot(scale, v25, 'k-', label='_nolegend_')
#pylab.plot(scale, vm04, 'k-', label='_nolegend_')
#pylab.plot(scale, vm05, 'k-', label='_nolegend_')
#pylab.plot(scale, vm06, 'k-', label='_nolegend_')

pylab.gca().set_ylim(-1.0, 1.8)
pylab.gca().set_xlim(0, 103)

# http://matplotlib.org/examples/pylab_examples/axhspan_demo.html
for s in scale:
    l = pylab.axvline(x=s, linewidth=0.5, color=(0,0,0,0), alpha=0.5)

ay1 = pylab.gca()
ay1.xaxis.set_ticks([n for n in scale])
ay1.xaxis.set_ticklabels(labels)
if 0:
    ay1.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
ay1.yaxis.set_ticks([-0.5, -0.2, -0.1, 0.0, 0.1, 0.2, 0.5, 1.3, 1.6, 1.7, 1.8, 1.9, 2.0, 2.3])
ay1.yaxis.set_ticklabels(['-0.5', '-0.2', '-0.1', '80%', '0.1', '0.2', '0.5', '-0.5', '-0.2', '-0.1', '90%', '0.1', '0.2', '0.5'])

for label in ay1.get_xticklabels() + ay1.get_yticklabels():
    label.set_fontsize(8)
# rotate labels http://old.nabble.com/Rotate-x-axes-%28xticks%29-text.-td3141258.html
for n, label in enumerate(ay1.get_xticklabels()):
    label.set_rotation(75)
    label.set_position((0.0,1.0 * (n % 2)))

for n, f in enumerate(files[1:]):
    color = colors[n % len(colors)]
    name = os.path.splitext(os.path.basename(f))[0]
    name = name.replace('.db_energies', '')
    name = name.replace('.remove', '')
    name = name.replace('rocksalt.', '')
    name = name.replace('fcc.', '')
    name = name.replace('espresso_gbrv_1.2.srel', 'ESPRESSO GBRV 1.2 USPP scalar-relativistic')
    name = name.replace('espresso_gbrv_1.4.srel', 'ESPRESSO GBRV 1.4 USPP scalar-relativistic')
    name = name.replace('espresso_sg15_oncv.srel', 'ESPRESSO SG15_ONCV NC scalar-relativistic')
    name = name.replace('espresso_sssp_accurate.srel', 'ESPRESSO SSSP 0.6 scalar-relativistic')
    name = name.replace('gpaw_paw09.nrel', 'GPAW PAW 0.9 non-relativistic')
    name = name.replace('gpaw_paw09.srel', 'GPAW PAW 0.9 scalar-relativistic')
    name = name.replace('aims_tier2.nrel', 'FHI-AIMS tier2 non-relativistic')
    name = name.replace('aims_tier2.srel', 'FHI-AIMS tier2 atomic_zora scalar')
    name = name.replace('elk.nrel', 'ELK 3.0.4 non-relativistic')
    name = name.replace('elk.srel', 'ELK 3.0.4 scalar-relativistic')
    name = name.replace('exciting.nrel', 'EXCITING BORON-9 non-relativistic')
    name = name.replace('exciting.zora', 'EXCITING BORON-9 zora')
    name = name.replace('exciting.iora*', 'EXCITING BORON-9 iora*')
    # field 2: 80%
    fref = 8  # 100% lattice constant
    f=2
    values = []
    for i, v in enumerate(data[n+1]):
        try:
            code = eval(v[f]) - eval(v[fref])
        except IndexError:
            code = np.nan
        #print name, i, data[0][i][0]
        if data[0][i][f] == 'nan' or data[0][i][fref] == 'nan':
            ref = np.nan
        else:
            ref = eval(data[0][i][f]) - eval(data[0][i][fref])
        #print v[0], code, ref, code - ref
        print v[0], v[f], v[fref], data[0][i][f], data[0][i][fref]
        values.append(code - ref)
        #print i, code-ref, code, ref
    print name, len(values)
    pylab.plot(scale, values, linestyle='-',
               marker=markers[n % len(markers)], color=color, label=name)
    # field 3: 90%
    f=4
    values = []
    for i, v in enumerate(data[n+1]):
        try:
            code = eval(v[f]) - eval(v[fref])
        except IndexError:
            code = np.nan
        if data[0][i][f] == 'nan' or data[0][i][fref] == 'nan':
            ref = np.nan
        else:
            ref = eval(data[0][i][f]) - eval(data[0][i][fref])
        #print v[0], code, ref, code - ref
        values.append(code - ref + 1.8)
        #print i, code-ref, code, ref
    pylab.plot(scale, values, linestyle='-',
               marker=markers[n % len(markers)], color=color, label='')

prop = matplotlib.font_manager.FontProperties(size=8)
leg = pylab.legend(loc='upper center', fancybox=True, prop=prop)
leg.get_frame().set_alpha(0.5)
# http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg03952.html
leg._loc=(0.02, 0.50)

t = pylab.title('Cell compression energy of bulk %s' % structure.replace('.',''))
# http://old.nabble.com/More-space-between-title-and-secondary-x-axis-td31722298.html
t.set_y(1.05)

pylab.xlabel('element')
pylab.ylabel('code - FHI-AIMS tier2 %s [eV]' % {
        'nrel': 'non-relativistic',
        'srel': 'relativistic atomic_zora scalar'}[relativistic])

pylab.savefig('%s_%s.png' % (structure.replace('.',''), relativistic),
              bbox_inches='tight', dpi=600)
