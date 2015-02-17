import matplotlib.pyplot as plt
import ase.db
con = ase.db.connect('cubic_perovskites.db')

rows = []
for i, line in enumerate(open('abo3.csv')):
    if line[0] == '#':
        continue
    id, formula = line.split(',')[:2]
    id = int(id)
    row = con.get(id)
    rows.append(row)
    plt.text(i - 1.25, -1.9, formula, rotation=60)

N = len(rows)
x = range(N)
y = [(row.VB_ind + row.CB_ind) / 2 - 4.5 for row in rows]
dyd = [row.gllbsc_dir_gap / 2 for row in rows]
dyi = [row.gllbsc_ind_gap / 2 for row in rows]
plt.errorbar(x, y, dyd, color='k', lw=0, mew=2, elinewidth=2,
             label='Direct Gap')
plt.errorbar(x, y, dyi, color='r', lw=0, mew=2, elinewidth=2,
             label='Indirect Gap')
plt.xlim(-1, N)
plt.ylim(4.4, -2.2)
plt.axhline(y=0, xmin=-1, xmax=N, lw=2, color='b', ls='dashed')
plt.axhline(y=1.23, xmin=-1, xmax=N, lw=2, color='g', ls='dotted')
plt.text(N + 0.1, 0.2, 'H$^+$/H$_2$', color='b')
plt.text(N + 0.1, 1.43, 'O$_2$/H$_2$O', color='g')
plt.ylabel('Potential (V vs NHE) [eV]')
plt.xticks([-1], '')
plt.legend(loc=4)
plt.savefig('abo3.svg')
