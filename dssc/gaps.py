import numpy as np
import matplotlib.pyplot as plt
import ase.db

c = ase.db.connect('dssc.db')
x = []
y = []
for dct in c.select(A='EthynPhA'):
    x.append(dct.de_gap)
    y.append(dct.ks_gap)
             
plt.plot(x, y, 'rx')
plt.plot(x, np.polyval(np.polyfit(x, y, 1), x))
plt.xlabel('KS-gap')
plt.ylabel('IP-EA')
plt.savefig('gaps.svg')
