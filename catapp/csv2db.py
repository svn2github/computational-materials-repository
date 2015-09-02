# creates: catapp.db
import csv
import ase.db
from ase import Atoms


reader = csv.reader(open('catappdata.csv'))
next(reader)  # skip header
with ase.db.connect('catapp.db', append=False) as con:
    for er, ea, surface, ab, a, b, ref, url, dataset in reader:
        if surface.startswith('HH- '):
            surf = surface[4:]
        else:
            surf = surface
        keys = {}
        words = surf.split()
        if len(words) == 2:
            surf, keys['site'] = words
        else:
            surf, = words
        symbols, facet = surf.split('(')
        facet = '(' + facet
        symbols = symbols.replace('-', '')
        atoms = Atoms(symbols, pbc=(True, True, False))
        a, b, ab = (x if x[:2] != 'hf' else x[2:] + '/2' for x in [a, b, ab])
        for xc in ['RPBE', 'PW91', 'BEEF']:
            if xc in dataset:
                break
        else:
            xc = '???'
        if ea:
            keys['ea'] = float(ea)
        con.write(atoms, a=a, b=b, ab=ab, er=float(er),
                  surface=surface, facet=facet,
                  xc=xc, ref=ref, url=url, dataset=dataset,
                  project='catapp', **keys)
