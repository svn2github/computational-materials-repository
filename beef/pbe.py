from ase.db import connect
from gpaw import GPAW, PW, Mixer, FermiDirac

cref = connect('beefgpaw.db')
xc = 'PBE'
names = [row.name for row in cref.select(xc=xc)]

c = connect('pbe.db')
for name in names:
    id = c.reserve(name=name)
    if id is None:
        continue
    atoms = cref.get_atoms(xc=xc, name=name)
    atoms.center(vacuum=3.5)
    atoms.cell += ([0, 0, 0], [0, 0.1, 0], [0, 0, 0.2])
    atoms.calc = GPAW(mode=PW(600),
                      xc=xc,
                      mixer=Mixer(0.25, 3, 1.0),
                      occupations=FermiDirac(0.0, fixmagmom=True),
                      txt=name + '.' + xc + '.txt')
    atoms.get_forces()
    c.write(atoms, name=name, xc=xc)
    del c[id]
