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
for row in con.select('g0w0_gap', sort='gw_gap'):
    data.append([row.formula,
                 row.gw_gap,
                 row.gw0_gap,
                 row.g0w0_gap,
                 row.lda_gap,
                 row.gllbsc_gap,
                 row.gllbsc_gap - row.gllbsc_disc,
                 row.hse06_gap])

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
