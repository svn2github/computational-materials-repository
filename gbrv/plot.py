import os

import numpy as np
from numpy import nan
import csv

import matplotlib
matplotlib.use('Agg')

from matplotlib import pylab

from ase.data import atomic_numbers

property = 'energy'
property = 'volume'

#category = 'fcc'
#category = 'bcc'
category = 'rocksalt'
#category = 'perovskite'
#category = 'halfheusler'

# http://matplotlib.org/examples/pylab_examples/line_styles.html
linestyles = ['_', '-', '--', ':']
markers = []
for m in matplotlib.lines.Line2D.markers:
    try:
        if len(m) == 1 and m != ' ':
            markers.append(m)
    except TypeError:
        pass

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
        if 1:  # this kills minus!
            if '--' in line:
                continue
        if 'np' in line:
            continue
        if line.startswith('c'):
            continue
        if 'N/A' in line:
            continue
        if not line.strip():
            continue
        yield line

files = [
    'gbrv_aims_tier2.db_' + category + '_raw.csv',
    'gbrv_exciting.db_' + category + '_raw.csv',
    'gbrv_gpaw_paw09.db_' + category + '_raw.csv',
    'gbrv_espresso_sg15_oncv24Jan2015.db_' + category + '_raw.csv',
    'gbrv_espresso_gbrv1.2.db_' + category + '_raw.csv',
    #'gbrv_dacapo_vanderbilt2.db_' + category + '_raw.csv',
    ]

if property == 'volume':
    files.append('wien2k_'+ category + '_raw.csv')
    files.append('vasp_'+ category + '_raw.csv')

eos = []
energy = []
labels = []
for n, f in enumerate(files):
    reader = csv.reader(CommentStripper(open(f, 'r')), delimiter=',')
    #reader = csv.reader(CommentStripper(open(f, 'r')), delimiter='\t')
    if n == 0:
        for r in reader:
            labels.append(r[0])
    reader = csv.reader(CommentStripper(open(f, 'r')), delimiter=',')
    #reader = csv.reader(CommentStripper(open(f, 'r')), delimiter='\t')
    d = {}
    for r in reader:
        d[r[0]] = float(r[3])
    eos.append(d)
    reader = csv.reader(CommentStripper(open(f, 'r')), delimiter=',')
    #reader = csv.reader(CommentStripper(open(f, 'r')), delimiter='\t')
    d = {}
    for r in reader:
        d[r[0]] = float(r[1])
    energy.append(d)


scale = [l for l in range(len(labels))]
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
v20 = [2.0 for v in scale]
v50 = [5.0 for v in scale]
v100 = [10.0 for v in scale]
v200 = [20.0 for v in scale]
v300 = [30.0 for v in scale]
v400 = [40.0 for v in scale]
v500 = [50.0 for v in scale]
vm01 = [-0.1 for v in scale]
vm02 = [-0.2 for v in scale]
vm05 = [-0.5 for v in scale]
vm10 = [-1.0 for v in scale]
vm20 = [-2.0 for v in scale]
vm50 = [-5.0 for v in scale]
vm100 = [-10.0 for v in scale]
vm200 = [-20.0 for v in scale]
vm300 = [-30.0 for v in scale]

#pylab.plot(scale, vm200, 'k-', label='_nolegend_')
#pylab.plot(scale, vm100, 'k-', label='_nolegend_')
pylab.plot(scale, vm50, 'k-', label='_nolegend_')
pylab.plot(scale, vm20, 'k-', label='_nolegend_')
pylab.plot(scale, vm10, 'k-', label='_nolegend_')
pylab.plot(scale, vm05, 'k-', label='_nolegend_')
#pylab.plot(scale, vm02, 'k-', label='_nolegend_')
#pylab.plot(scale, vm01, 'k-', label='_nolegend_')
pylab.plot(scale, zero, 'k-', label='_nolegend_')
#pylab.plot(scale, v01, 'k-', label='_nolegend_')
#pylab.plot(scale, v02, 'k-', label='_nolegend_')
pylab.plot(scale, v05, 'k-', label='_nolegend_')
pylab.plot(scale, v10, 'k-', label='_nolegend_')
pylab.plot(scale, v20, 'k-', label='_nolegend_')
pylab.plot(scale, v50, 'k-', label='_nolegend_')
#pylab.plot(scale, v100, 'k-', label='_nolegend_')
#pylab.plot(scale, v200, 'k-', label='_nolegend_')
#pylab.plot(scale, v300, 'k-', label='_nolegend_')
#pylab.plot(scale, v400, 'k-', label='_nolegend_')
#pylab.plot(scale, v500, 'k-', label='_nolegend_')

pylab.gca().set_ylim(-5., 5.)
pylab.gca().set_xlim(-1, max(scale) + 1)

# http://matplotlib.org/examples/pylab_examples/axhspan_demo.html
for s in scale:
    l = pylab.axvline(x=s, linewidth=0.5, color=(0,0,0,0), alpha=0.5)

ay1 = pylab.gca()
ay1.xaxis.set_ticks([n for n in scale])
ay1.xaxis.set_ticklabels(labels)
if 0:
    ay1.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
else:
    ay1.yaxis.set_ticks([-2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0])
    ay1.yaxis.set_ticklabels(['-2.0', '-1.0', '-0.5', '0.0', '0.5', '1.0', '2.0'])

for label in ay1.get_xticklabels() + ay1.get_yticklabels():
    label.set_fontsize(8)
# rotate labels http://old.nabble.com/Rotate-x-axes-%28xticks%29-text.-td3141258.html
for n, label in enumerate(ay1.get_xticklabels()):
    label.set_rotation(75)
    label.set_position((0.0,1.0 * (n % 2)))

for n, f in enumerate(files[1:]):
    color = colors[n % len(colors)]
    name = f
    name = name.replace('_raw.csv', '')
    name = name.replace('.db_', '')
    name = name.replace('gbrv_espresso_gbrv1.2'  + category,
                        'ESPRESSO GBRV 1.2 USPP scalar-relativistic')
    name = name.replace('gbrv_espresso_sg15_oncv24Jan2015' + category,
                        'ESPRESSO SG15_ONCV NC scalar-relativistic')
    name = name.replace('gbrv_dacapo_vanderbilt2' + category,
                        'DACAPO Vanderbilt USPP scalar-relativistic')
    name = name.replace('gbrv_gpaw_paw09' + category,
                        'GPAW PAW 0.9 scalar-relativistic')
    name = name.replace('gbrv_aims_tier2'  + category,
                        'FHI-AIMS tier2 relativistic atomic_zora scalar')
    name = name.replace('gbrv_exciting' + category,
                        'BORON-9 iora*')
    name = name.replace('wien2k_'+ category, 'WIEN2K / 10.1016/j.commatsci.2013.08.053')
    name = name.replace('vasp_'+ category, 'VASP / 10.1016/j.commatsci.2013.08.053')
    if property == 'volume':
        p = eos
    else:
        p = energy
    values = []
    for l in labels:
        try:
            v = p[n+1][l]
        except KeyError:
            v = np.nan
        if property == 'volume':
            v = (v-p[0][l]) / p[0][l] * 100
        else:
            v = (v-p[0][l])
        values.append(v)
    avg =  np.std([v for v in values if not np.isnan(v)])
    pylab.plot(scale, values, linestyle='-',
               marker=markers[n % len(markers)], color=color,
               label=name + ': stddev = ' + str(round(avg, 2)))

prop = matplotlib.font_manager.FontProperties(size=10)
leg = pylab.legend(loc='lower right', fancybox=True, prop=prop)
leg.get_frame().set_alpha(0.5)
# http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg03952.html
leg._loc=(0.01, 0.02)

t = pylab.title('PBE ' + category + ': ' + {'volume': 'volume', 'energy': 'formation energy'}[property])
# http://old.nabble.com/More-space-between-title-and-secondary-x-axis-td31722298.html
t.set_y(1.05)

pylab.xlabel('compound')
if property == 'volume':
    pylab.ylabel('% difference wrt. FHI-AIMS tier2 atomic_zora scalar')
else:
    pylab.ylabel('difference wrt. FHI-AIMS tier2 atomic_zora scalar [eV]')

pylab.savefig('gbrv_%s_%s.png' % (category, property), bbox_inches='tight', dpi=600)
