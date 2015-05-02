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

postfix = '.remove.db'
#postfix = '.db'

files = [
    #'nwchem_def2-qzvppd.nrel.PBE' + postfix + '.csv',
    #'nwchem_aug-cc-pv5z.nrel.PBE' + postfix + '.csv',
    #'nwchem_aug-cc-pvqz.nrel.PBE' + postfix + '.csv',
    #'aims_tight.nrel.PBE' + postfix + '.csv',
    'aims_tight.srel.PBE' + postfix + '.csv',  # this
    #'aims_tier2.nrel.PBE' + postfix + '.csv',
    'aims_tier2.srel.PBE' + postfix + '.csv',  # this
    'espresso_pslib_0.3.1.srel.PBE' + postfix + '.csv',  # this
    #'espresso_gbrv_1.2.srel.PBE' + postfix + '.csv',
    'espresso_gbrv_1.4.srel.PBE' + postfix + '.csv',  # this
    'espresso_sg15_oncv.srel.PBE' + postfix + '.csv',  # this
    #'gpaw_paw09.nrel.PBE' + postfix + '.csv',
    'gpaw_paw09.srel.PBE' + postfix + '.csv',  # this
    #'tmfp06d_exp' + postfix + '.csv',
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

pylab.plot(scale, zero, 'k-', label='_nolegend_')
pylab.plot(scale, vm01, 'k-', label='_nolegend_')
pylab.plot(scale, vm02, 'k-', label='_nolegend_')
pylab.plot(scale, v01, 'k-', label='_nolegend_')
pylab.plot(scale, v02, 'k-', label='_nolegend_')
pylab.plot(scale, v06, 'k-', label='_nolegend_')
pylab.plot(scale, v07, 'k-', label='_nolegend_')
pylab.plot(scale, v08, 'k-', label='_nolegend_')
pylab.plot(scale, v09, 'k-', label='_nolegend_')
pylab.plot(scale, v10, 'k-', label='_nolegend_')
pylab.plot(scale, v11, 'k-', label='_nolegend_')
pylab.plot(scale, v14, 'k-', label='_nolegend_')
pylab.plot(scale, v15, 'k-', label='_nolegend_')
pylab.plot(scale, v16, 'k-', label='_nolegend_')
pylab.plot(scale, v17, 'k-', label='_nolegend_')
pylab.plot(scale, v18, 'k-', label='_nolegend_')

pylab.gca().set_ylim(-0.6, 4.1)
pylab.gca().set_xlim(0, len(labels) - 1)

# http://matplotlib.org/examples/pylab_examples/axhspan_demo.html
for s in scale:
    l = pylab.axvline(x=s, linewidth=0.5, color=(0,0,0,0), alpha=0.5)

ay1 = pylab.gca()
ay1.xaxis.set_ticks([n for n in scale])
ay1.xaxis.set_ticklabels(labels)
if 0:
    ay1.yaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())
ay1.yaxis.set_ticks([-0.2, -0.1, 0.0, 0.1, 0.2, 0.6, 0.7, 0.8, 0.9, 1.0, 1.4, 1.5, 1.6, 1.7, 1.8])
ay1.yaxis.set_ticklabels(['-0.2', '-0.1', '$D_{e}$', '0.1', '0.2',
                          '-2', '-1', '$r_{e}$', '1', '2',
                          '-20', '-10', '$\omega_{e}$', '10', '20'])

for label in ay1.get_xticklabels() + ay1.get_yticklabels():
    label.set_fontsize(10)
# rotate labels http://old.nabble.com/Rotate-x-axes-%28xticks%29-text.-td3141258.html
for n, label in enumerate(ay1.get_xticklabels()):
    label.set_rotation(75)
    label.set_position((0.0,1.0 * (n % 2)))


for n, f in enumerate(files[1:]):
    color = colors[n % len(colors)]
    name = os.path.splitext(os.path.basename(f))[0]
    name = name.replace('.db', '')
    name = name.replace('.remove', '')
    name = name.replace('nwchem_aug-cc-pv5z.nrel.PBE', 'PBE NWCHEM aug-cc-pv5z non-relativistic')
    name = name.replace('nwchem_aug-cc-pvqz.nrel.PBE', 'PBE NWCHEM aug-cc-pvqz non-relativistic')
    name = name.replace('nwchem_def2-qzvppd.nrel.PBE', 'PBE NWCHEM def2-qzppd non-relativistic')
    name = name.replace('espresso_pslib_0.3.1.srel.PBE', 'PBE ESPRESSO PSLibrary 0.3.1 PAW scalar-relativistic')
    name = name.replace('espresso_gbrv_1.2.srel.PBE', 'PBE ESPRESSO GBRV 1.2 USPP scalar-relativistic')
    name = name.replace('espresso_gbrv_1.4.srel.PBE', 'PBE ESPRESSO GBRV 1.4 USPP scalar-relativistic')
    name = name.replace('espresso_sg15_oncv.srel.PBE', 'PBE ESPRESSO SG15_ONCV NC scalar-relativistic')
    name = name.replace('gpaw_paw09.nrel.PBE', 'PBE GPAW PAW 0.9 non-relativistic')
    name = name.replace('gpaw_paw09.srel.PBE', 'PBE GPAW PAW 0.9 scalar-relativistic')
    name = name.replace('aims_tier2.nrel.PBE', 'PBE FHI-AIMS tier2 non-relativistic')
    name = name.replace('aims_tier2.srel.PBE', 'PBE FHI-AIMS tier2 atomic_zora scalar')
    name = name.replace('aims_tight.nrel.PBE', 'PBE FHI-AIMS tight non-relativistic')
    name = name.replace('aims_tight.srel.PBE', 'PBE FHI-AIMS tight atomic_zora scalar')
    name = name.replace('tmfp06d_exp', 'experimental')
    # column 2: atomization energy relaxed
    c = 2
    values = []
    for i, v in enumerate(data[n+1]):
        try:
            value = eval(v[c]) - eval(data[0][i][c])
        except IndexError:
            value = np.nan
        values.append(value)
    s2 = np.std([i for i in values if not np.isnan(i)])
    pylab.plot(scale, values, linestyle='-',
               marker=markers[n % len(markers)], color=color, label='')
    # column 3: atomic distance
    c = 3
    values = []
    for i, v in enumerate(data[n+1]):
        try:
            if 0 and name == 'FHI-AIMS tight non-relativistic':
                print i, eval(v[c]), eval(data[0][i][c])
            value = (eval(v[c]) - eval(data[0][i][c])) * 10 + 0.8
        except IndexError:
            value = np.nan
        values.append(value)
    s3 = np.std([i for i in values if not np.isnan(i)])
    pylab.plot(scale, values, linestyle='-',
               marker=markers[n % len(markers)], color=color, label='')
    # column 5: harmonic frequency
    c = 5
    values = []
    for i, v in enumerate(data[n+1]):
        try:
            if 0 and name == 'FHI-AIMS tight non-relativistic':
                print i, eval(v[c]), eval(data[0][i][c])
            value = (eval(v[c]) - eval(data[0][i][c])) / 100 + 0.8 + 0.8
        except IndexError:
            value = np.nan
        values.append(value)
    s5 = np.std([i for i in values if not np.isnan(i)])
    pylab.plot(scale, values, linestyle='-',
               marker=markers[n % len(markers)], color=color,
               label=name + ", stddev: $D_{e}$ %.2f, $r_{e}$ %.1f, $\omega_{e}$ %.1f" % (s2, s3*10, s5*100))

prop = matplotlib.font_manager.FontProperties(size=10)
leg = pylab.legend(loc='lower left', fancybox=True, prop=prop)
leg.get_frame().set_alpha(0.5)
# http://www.mail-archive.com/matplotlib-users@lists.sourceforge.net/msg03952.html
leg._loc=(0.01, 0.70)

t = pylab.title('Properties of dimers (doi:10.1063/1.2162161):\n\natomization energy $D_{e}$ [eV], bondlength $r_{e}$ [pm], harmonic frequency $\omega_{e}$ [1/cm]', fontsize=11)
# http://old.nabble.com/More-space-between-title-and-secondary-x-axis-td31722298.html
t.set_y(1.05)

pylab.xlabel('molecule')
#pylab.ylabel('code - NWCHEM non-relativistic (def2-qzvppd basis)')
pylab.ylabel('code - FHI-AIMS tight atomic_zora scalar')

pylab.savefig('tmfp06d.png', bbox_inches='tight', dpi=600)
