# creates: gaps.svg
import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as colors
import matplotlib.cm as cm
import ase.db

con = ase.db.connect('funct_perovskites.db')

n = 6
comb_A = 'BaSnO3'
comb_B = 'BaTaO2N'

matrix = []
gaps = []

for nA in range(1,n+1):
    vect = []
    for nB in range(1,n+1):
        name = ''
        for i in range(0,nA):
            name += 'A'
        for i in range(0,nB):
            name += 'B'
        gap = 0
        for dct in con.select(comb_A=comb_A, comb_B=comb_B, sequence=name):
            gap = dct.gllbsc_gamma_gap
        vect.append(gap)
        gaps.append(gap)
    vect.append(gap)
    matrix.append(np.array(vect))
matrix.append(np.array(vect))

colors = []
for i in gaps:
    c = cm.jet(int(float(i)/float(max(gaps))*255))
    for j in range(6):
        colors.append([c[0],c[1],c[2]])

x = np.array(range(1, 7), float)
y = x.copy()
xpos, ypos = np.meshgrid(x, y)
z = np.array(matrix)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros_like(xpos)
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = z.flatten()
fig = plt.figure()
ax = Axes3D(fig)
plt.xlabel('nB, B = '+comb_B)
plt.ylabel('nA, A = '+comb_A)
ax.set_zlabel('Bandgap [eV]')
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)
plt.savefig('gaps.svg')
plt.show()
