import os
import time

import copy

import numpy as np

import ase.db
from ase.structure import molecule
from ase.optimize.bfgs import BFGS
from ase.calculators.nwchem import NWChem
from ase.data.g2 import data
from ase.data.g2 import molecule_names, atom_names

c = ase.db.connect('nwchem.db')

basis = 'def2-qzvppd'

code = 'nwchem' + '_' + basis

names = molecule_names

for formula in names:
    atoms = molecule(formula, data=data)

    elements_bsse = {}
    elements = {}

    elements_bsse[formula] = atoms
    elements[formula] = atoms

    for n, a in enumerate(atoms):
        #print n,
        name = formula + '_bq' + str(n)
        mbq = copy.deepcopy(atoms)
        tags = np.zeros(len(atoms))
        tags = [-71 for t in tags]  # bq atoms
        tags[n] = 0 # real atom
        mbq.set_tags(tags)
        # get charge and magnetic moment of the real atom
        index = list(tags).index(0)
        symbol = mbq.get_chemical_symbols()[index]
        atom = molecule(symbol, data=data)
        magmoms = np.zeros(len(atoms))
        magmoms[index] = atom[0].magmom
        charges = np.zeros(len(atoms))
        charges[index] = atom[0].charge
        mbq.set_initial_magnetic_moments(magmoms)
        mbq.set_initial_charges(charges)
        elements_bsse[name] = mbq
        elements[symbol] = atom
        #print name, mbq.get_tags()

    skeys = elements_bsse.keys()
    skeys.sort()
    for f in skeys:
        compound = elements_bsse[f]
        id = c.reserve(name=f, basis=basis, bsse=True)
        if id is None:
            continue
        fullbasis = ''
        firsttime = {}
        for i, tag in enumerate(compound.get_tags()):
            symbol = compound[i].symbol
            print f, i, symbol, tag
            if tag: # ghost atom bq
                if firsttime.get('bq' + symbol, 1):
                    fullbasis += 'bq' + symbol + ' library ' + symbol + ' ' + basis + '\n'
                    firsttime['bq' + symbol] = 0
            else:
                if firsttime.get(symbol, 1):
                    fullbasis += symbol + ' library ' + symbol + ' ' + basis + '\n'
                    firsttime[symbol] = 0
        label = f + '_' + code
        print label, compound.get_tags(), fullbasis
        calc = NWChem(geometry='noautosym nocenter noautoz',
                      task='gradient',
                      xc='PBE',
                      grid='nodisk',
                      tolerances='tight',
                      maxiter=777,
                      convergence={'lshift': 0.0},
                      basis=fullbasis,
                      basispar='spherical',
                      direct='noio',
                      #raw='set int:txs:limxmem 20485760208\nmemory total 20000 Mb noverify\n',
                      label=label)
        compound.set_calculator(calc)
        t = time.time()
        compound.get_potential_energy()
        c.write(compound, name=f, relaxed=False, basis=basis, bsse=True,
                time=time.time()-t)
    del c[id]
