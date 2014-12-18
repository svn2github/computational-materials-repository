# creates: gaps.svg
"""Plot the GLLB-SC, HSE06, GW approximations bandgaps for a
set of 20 ternary and quaternary materials"""

import re
import numpy as np
import matplotlib.pyplot as plt
import ase.db

# Connect to database:
con = ase.db.connect('mp_gllbsc.db')

# Extract gaps data:
data = []
for dct in con.select('g0w0_gap'):
    data.append([dct.formula,
                 dct.gw_gap,
                 dct.gw0_gap,
                 dct.g0w0_gap,
                 dct.lda_gap,
                 dct.gllbsc_gap,
                 dct.gllbsc_gap - dct.gllbsc_disc,
                 dct.hse06_gap])
data.sort(key=lambda gaps: gaps[1])

# Make a bar-chart:
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(1, 1, 1)

w = 0.25  # width of bars
x = np.arange(len(data))
i = 1
for color, shift, label in [('y', 0, 'GW'),
                            ('m', 0, 'GW$_0$'),
                            ('r', 0, 'G$_0$W$_0$'),
                            ('k', 0, 'LDA'),
                            ('b', w, 'GLLB-SC - $\Delta_{xc}$'),
                            ('c', w, 'GLLB-SC - KS'),
                            ('g', 2 * w, 'HSE06')]:
    rects = ax.bar(x + shift, [gaps[i] for gaps in data], w,
                   color=color, label=label)
    i += 1

plt.legend(loc=2)
ax.set_ylabel('Bandgap at $\Gamma$ [eV]')
ax.set_xticks(x + w)
names = [re.sub(r'(\d+)', r'$_\1$', gaps[0]) for gaps in data]
ax.set_xticklabels(names, rotation=60)
plt.tight_layout()
plt.savefig('gaps.svg')
