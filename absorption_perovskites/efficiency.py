# creates: efficiency.svg
"""Plot the efficiencies of a perovskite phase (cubic in the example
here)"""

import matplotlib.pyplot as plt
import ase.db

# Connect to database:
c = ase.db.connect('absorption_perovskites.db')

o = open('perfect_abs.txt','r')
lines = o.readlines()
o.close()

en = []
perf_abs = []
for line in lines:
    line = line.split()
    en.append(float(line[0]))
    perf_abs.append(float(line[2])/4.30E+21)

for n in c.select('phase=cubic'):
    if 'O3' in n.name:
        color = 'black'
        symb = 'o'
    if 'O2N' in n.name or 'ON2' in n.name:
        color = 'red'
        symb = 's'
    if 'O2F' in n.name:
        color = 'blue'
        symb = 'D'

    plt.plot([n.gllbsc_ind_gap,n.gllbsc_ind_gap],[n.eff,n.eff_max],'-'+symb,color=color)
    plt.text(n.gllbsc_ind_gap-0.025,n.eff,n.name,color=color,fontsize=12,rotation=90,horizontalalignment='center',verticalalignment='bottom')

plt.plot(en,perf_abs,'--',color='green')
plt.plot(2.5,0.32,'o',color='black')
plt.plot(2.5,0.29,'s',color='red')
plt.plot(2.5,0.26,'D',color='blue')
plt.text(2.55,0.32,'Oxides',color='black',fontsize=16,horizontalalignment='left',verticalalignment='center')
plt.text(2.55,0.29,'Oxynitrides',color='red',fontsize=16,horizontalalignment='left',verticalalignment='center')
plt.text(2.55,0.26,'Oxyfluorides',color='blue',fontsize=16,horizontalalignment='left',verticalalignment='center')
plt.text(1.3,0.33,'Cubic',color='black',fontsize=16,horizontalalignment='left',verticalalignment='center')
plt.xlim(1.2,3.1)
plt.ylim(0,0.35)
plt.xlabel('Bandgap [eV]',fontsize=18)
plt.ylabel('Absorbed Photons [%]',fontsize=18)
plt.xticks([1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0],['1.4','1.6','1.8','2.0','2.2','2.4','2.6','2.8','3.0'],fontsize=16)
plt.yticks([0,0.05,0.1,0.15,0.2,0.25,0.3],['0','5','10','15','20','25','30'],fontsize=16)
plt.savefig('efficiency.svg')
