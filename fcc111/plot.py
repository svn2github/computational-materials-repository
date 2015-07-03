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
        if 'N/A' in line:
            continue
        if not line.strip():
            continue
        yield line

files = [
    'fcc111_aims_tier2.db_raw.csv',
    #'fcc111_aims_light.db_raw.csv',
    'fcc111_aims_tight.db_raw.csv',
    'fcc111_dacapo_vanderbilt2.db_raw.csv',
    #'fcc111_espresso_gbrv1.2.db_raw.csv',
    #'fcc111_espresso_pslib0.3.1.db_raw.csv',
    'fcc111_espresso_sg15_oncv24Jan2015.db_raw.csv',
    #'fcc111_gpaw_gpaw08.db_raw.csv',
    'fcc111_gpaw_gpaw09.db_raw.csv',
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
v03 = [0.3 for v in scale]
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
v24 = [2.4 for v in scale]
v25 = [2.5 for v in scale]
v26 = [2.6 for v in scale]
v27 = [2.7 for v in scale]
v28 = [2.8 for v in scale]
v29 = [2.9 for v in scale]
v30 = [3.0 for v in scale]
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
pylab.plot(scale, v05, 'k-', label='_nolegend_')
pylab.plot(scale, v20, 'k-', label='_nolegend_')
pylab.plot(scale, v23, 'k-', label='_nolegend_')
pylab.plot(scale, v24, 'k-', label='_nolegend_')
pylab.plot(scale, v25, 'k-', label='_nolegend_')
pylab.plot(scale, v26, 'k-', label='_nolegend_')
pylab.plot(scale, v27, 'k-', label='_nolegend_')
pylab.plot(scale, v30, 'k-', label='_nolegend_')


pylab.gca().set_ylim(-1.1, 3.6)
pylab.gca().set_xlim(0, 103)

# http://matplotlib.org/examples/pylab_examples/axhspan_demo.html
for s in scale:
    l = pylab.axvline(x=s, linewidth=0.5, color=(0,0,0,0), alpha=0.5)

ay1 = pylab.gca()
ay1.xaxis.set_ticks([n for n in scale])
ay1.xaxis.set_ticklabels(labels)
ay1.yaxis.set_ticks([-0.5, -0.2, -0.1, 0.0, 0.1, 0.2, 0.5, 2.0, 2.3, 2.4, 2.5, 2.6, 2.7, 3.0])
ay1.yaxis.set_ticklabels(['-0.5', '-0.2', '-0.1', 'Oxygen', '0.1', '0.2', '0.5', '-0.5', '-0.2', '-0.1', 'Carbon', '0.1', '0.2', '0.5'])

for label in ay1.get_xticklabels() + ay1.get_yticklabels():
    label.set_fontsize(8)
# rotate labels http://old.nabble.com/Rotate-x-axes-%28xticks%29-text.-td3141258.html
for n, label in enumerate(ay1.get_xticklabels()):
    label.set_rotation(75)
    label.set_position((0.0,1.0 * (n % 2)))

for n, f in enumerate(files[1:]):
    color = colors[n % len(colors)]
    name = os.path.splitext(os.path.basename(f))[0]
    name = name.replace('fcc111_', '')
    name = name.replace('fcc111.', '')
    name = name.replace('.db_raw', '')
    name = name.replace('espresso_pslib0.3.1', 'ESPRESSO PSLibrary 0.3.1 PAW scalar-relativistic')
    name = name.replace('espresso_gbrv1.2', 'ESPRESSO GBRV 1.2 USPP scalar-relativistic')
    name = name.replace('espresso_gbrv1.4', 'ESPRESSO GBRV 1.4 USPP scalar-relativistic')
    name = name.replace('espresso_sg15_oncv24Jan2015', 'ESPRESSO SG15_ONCV NC scalar-relativistic')
    name = name.replace('dacapo_vanderbilt2', 'DACAPO Vanderbilt USPP scalar-relativistic')
    name = name.replace('gpaw_gpaw08', 'GPAW PAW 0.8 scalar-relativistic')
    name = name.replace('gpaw_gpaw09', 'GPAW PAW 0.9 scalar-relativistic')
    name = name.replace('600', 'GPAW PAW 0.10 scalar-relativistic 600 eV')
    name = name.replace('550', 'GPAW PAW 0.10 scalar-relativistic 550 eV')
    name = name.replace('500', 'GPAW PAW 0.10 scalar-relativistic 500 eV')
    name = name.replace('h18', 'GPAW PAW 0.10 scalar-relativistic h=0.18')
    name = name.replace('h16', 'GPAW PAW 0.10 scalar-relativistic h=0.16')
    name = name.replace('h14', 'GPAW PAW 0.10 scalar-relativistic h=0.14')
    name = name.replace('aims_tier2', 'FHI-AIMS tier2 relativistic atomic_zora scalar')
    name = name.replace('aims_light', 'FHI-AIMS light relativistic atomic_zora scalar')
    name = name.replace('aims_tight', 'FHI-AIMS tight relativistic atomic_zora scalar')
    # field 9: total time
    values = []
    for i, v in enumerate(data[n+1]):
        values.append(float(eval(v[9])))
    # avg time
    ntime = np.mean([i for i in values if not np.isnan(i)])
    # field 8: total number of iterations
    values = []
    for i, v in enumerate(data[n+1]):
        values.append(float(eval(v[8])))
    # no. of converged systems
    nconv = len([1 for i in values if not np.isnan(i)])
    # avg number of iterations
    niter = np.mean([i for i in values if not np.isnan(i)])
    niter = 0  # nans not handled
    # adsorption of O
    values = []
    for i, v in enumerate(data[n+1]):
        vi = eval(v[2]) - eval(v[1]) - eval(v[4])
        v0 = eval(data[0][i][2]) - eval(data[0][i][1]) - eval(data[0][i][4])
        values.append(vi - v0)
    pylab.plot(scale, values, linestyle='-', marker=markers[n % len(markers)], color=color,
               #label=name + ', converged: ' + str(nconv) + '/73, avg(iter): ' + str(int(niter)))
               #label=name + ',avg(iter): ' + str(int(niter)))
               label=name)
    # adsorption of C
    values = []
    for i, v in enumerate(data[n+1]):
        vi = eval(v[3]) - eval(v[1]) - eval(v[5])
        v0 = eval(data[0][i][3]) - eval(data[0][i][1]) - eval(data[0][i][5])
        values.append(vi - v0 + 2.5)
    pylab.plot(scale, values, linestyle='-', marker=markers[n % len(markers)], color=color,
               label='')

prop = matplotlib.font_manager.FontProperties(size=8)
leg = pylab.legend(loc='upper center', fancybox=True, prop=prop)
leg.get_frame().set_alpha(0.5)
# http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg03952.html
leg._loc=(0.02, 0.45)

t = pylab.title('Adsorption energy of atomic oxygen and carbon on fcc111')
# http://old.nabble.com/More-space-between-title-and-secondary-x-axis-td31722298.html
t.set_y(1.05)

pylab.xlabel('element')
pylab.ylabel('code - FHI-AIMS tier2 relativistic atomic_zora scalar [eV]')

pylab.savefig('fcc111.png', bbox_inches='tight', dpi=600)
