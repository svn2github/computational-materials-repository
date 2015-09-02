# creates: WS_pourbaix.png
import numpy as np
import ase.db
from ase.phasediagram import Pourbaix, solvated

con = ase.db.connect('cubic_perovskites.db')

pH = 7.
Us = np.arange(-1, 2, 0.1)
E0 = -4.5
lb = -0.5  # lower bound for the energy scale
ub = 2.0  # upper bound for the energy scale

info = []
xs = []
ys = []
heats = []

for row in con.select('heat_of_formation_all<=0.21'):
    if (row.gllbsc_ind_gap >= 1.4 and row.gllbsc_ind_gap <= 3.1 and
        row.CB_ind <= 0 - E0 and row.VB_ind >= 1.23 - E0) or \
       (row.gllbsc_dir_gap >= 1.4 and row.gllbsc_dir_gap <= 3.1 and
        row.CB_dir <= 0 - E0 and row.VB_dir >= 1.23 - E0):
        name = row.A_ion + row.B_ion + row.anion
        energy = row.standard_energy

        info.append([name, row.gllbsc_ind_gap + E0, row.gllbsc_dir_gap + E0,
                     row.VB_ind + E0, row.CB_ind + E0,
                     row.VB_dir + E0, row.CB_dir + E0])

        refs = []
        for row_ref in con.select('reference'):
            refs.append((row_ref.formula, row_ref.standard_energy))

        # Extract the dissolved phases:
        refs += solvated(row.A_ion + row.B_ion)

        for U in Us:
            pb = Pourbaix(refs, name)
            results, refs_energy = pb.decompose(U, pH, verbose=False)
            Ediff = (energy - refs_energy) / 5
            Ediff = min(Ediff, ub)
            Ediff = max(Ediff, lb)
            xs.append(len(info) - 1)
            ys.append(U)
            heats.append(Ediff)

import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.collections import PatchCollection
import matplotlib.patches as patches

fig = plt.figure(figsize=(20, 16))
ax = fig.add_subplot(111)

cx = 0.3
cy = 0.05
rects = []
for i in range(len(heats)):
    rect = patches.Rectangle((xs[i] - cx, ys[i] - cy), 2 * cx, 2 * cy)
    rects.append(rect)
p = PatchCollection(rects, edgecolors=None, linewidths=0, cmap=cm.RdYlGn_r)
p.set_array(np.array(heats))
ax.add_collection(p)

for i in range(len(info)):
    plt.plot([i - cx, i + cx], [info[i][3], info[i][3]], '-',
             color='k', linewidth=3)
    plt.plot([i - cx, i + cx], [info[i][4], info[i][4]], '-',
             color='k', linewidth=3)
    plt.plot([i - cx, i + cx], [info[i][5], info[i][5]], '-',
             color='r', linewidth=3)
    plt.plot([i - cx, i + cx], [info[i][6], info[i][6]], '-',
             color='r', linewidth=3)
    plt.text(i, 2.5, round(info[i][1], 1), color='k', fontsize=17.5,
             verticalalignment='top', horizontalalignment='center')
    plt.text(i, 2.75, round(info[i][2], 1), color='r', fontsize=17.5,
             verticalalignment='top', horizontalalignment='center')
plt.plot([cx, cx], [info[0][3], info[0][3]], '-', color='k', linewidth=3,
         label='Indirect BE')
plt.plot([cx, cx], [info[0][5], info[0][5]], '-', color='r', linewidth=3,
         label='Direct BE')
plt.text(len(info) + 1.5, 2.5, 'Indirect BG', color='k', fontsize=17.5,
         verticalalignment='top', horizontalalignment='left')
plt.text(len(info) + 1.5, 2.75, 'Direct BG', color='r', fontsize=17.5,
         verticalalignment='top', horizontalalignment='left')

for i in range(len(info)):
    formula = info[i][0]
    for j in range(10):
        if str(j) in formula:
            formula = formula.replace(str(j), "$_" + str(j) + "$")
    plt.text(i - cx, -1.25, formula, rotation=60, va='bottom', ha='left',
             fontsize=20.5, color='k')

xmax = len(info) + 4
plt.text(xmax + 0.05, -1, 'pH$=' + str(pH) + '$', color='black', fontsize=20.5,
         verticalalignment='center')
plt.axhline(1.23, xmin=0, xmax=xmax, color='g', ls='dotted', lw=3.5)
plt.text(xmax + 0.05, 1.23, 'O$_2$/H$_2$O', color='g', fontsize=16.5)
plt.axhline(0, xmin=0, xmax=xmax, color='b', ls='dashed', lw=3.5)
plt.text(xmax + 0.05, 0, 'H$^+$/H$_2$', color='b', fontsize=16.5)

cbar = plt.colorbar(p, orientation='horizontal', shrink=0.5)
cbar.set_label('$\Delta E$ [eV/atom]', fontsize=24.5)

plt.ylabel('$E$ [V vs NHE]', fontsize=26.5)
plt.yticks([-1, -0.5, 0, 0.5, 1, 1.5, 2],
           ['-1.0', '-0.5', '0.0', '0.5', '1.0', '1.5', '2.0'],
           fontsize=18.5)
plt.xticks([])
plt.legend()
plt.xlim(xmin=-0.5, xmax=xmax)
plt.ylim(ymin=-2.3, ymax=2.9)
plt.gca().invert_yaxis()

plt.savefig('WS_pourbaix.png')
