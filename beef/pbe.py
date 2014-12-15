from ase.db import connect
from gpaw import GPAW, PW

cref = connect('beefgpaw.db')
xc = 'PBE'
names = [d.name for d in cref.select(xc=xc)]

c = connect('pbe.db')
for name in names:
    id = c.reserve(name=name)
    if id is None:
        continue
    atoms = cref.get_atoms(xc=xc, name=name)
    atoms.center(vacuum=3.5)
    atoms.calc = GPAW(mode=PW(600),
                      txt=name + '.' + xc + '.txt')
    atoms.get_forces()
    c.write(atoms, name=name, xc=xc)
    del c[id]
