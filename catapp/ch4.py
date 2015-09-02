# creates: ch4.svg
import matplotlib.pyplot as plt
import ase.db

con = ase.db.connect('catapp.db')
x = []
y = []
for row in con.select(a='H*', b='CH3*'):
    x.append(row.er)
    y.append(row.ea)
    
plt.plot(x, y, 'o', label='H*+CH3*->CH4')
plt.legend()
plt.xlabel('reaction energy [eV]')
plt.ylabel('activation energy [eV]')
plt.savefig('ch4.svg')
