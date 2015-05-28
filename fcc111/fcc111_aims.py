import os
import sys
import time

import numpy as np

import ase.db
from ase.utils import opencew
from ase.data import chemical_symbols
from ase.lattice import bulk
from ase.lattice.surface import fcc111, add_adsorbate
from ase.constraints import FixAtoms
from ase.optimize.bfgs import BFGS
from ase.calculators.calculator import kpts2mp
from ase.io.trajectory import PickleTrajectory

# fcc lattice constant
# PBE FHI-AIMS tight, relativistic atomic_zora scalar
fcc = {
    'H':  2.28,
    'He': 4.16,
    'Li': 4.32,
    'Be': 3.15,
    'B':  2.87,
    'C':  3.08,
    'N':  3.12,
    'O':  3.17,
    'F':  3.43,
    'Ne': 4.61,
    'Na': 5.32,
    'Mg': 4.52,
    'Al': 4.04,
    'Si': 3.87,
    'P':  3.87,
    'S':  3.99,
    'Cl': 4.39,
    'Ar': 5.94,
    'K':  6.67,
    'Ca': 5.52,
    'Sc': 4.62,
    'Ti': 4.11,
    'V':  3.81,
    'Cr': 3.62,
    'Mn': 3.50,
    'Fe': 3.45,
    'Co': 3.45,
    'Ni': 3.51,
    'Cu': 3.63,
    'Zn': 3.93,
    'Ga': 4.23,
    'Ge': 4.28,
    'As': 4.25,
    'Se': 4.33,
    'Br': 4.72,
    'Kr': 6.42,
    'Rb': 7.15,
    'Sr': 6.02,
    'Y':  5.06,
    'Zr': 4.52,
    'Nb': 4.22,
    'Mo': 4.00,
    'Tc': 3.87,
    'Ru': 3.81,
    'Rh': 3.83,
    'Pd': 3.94,
    'Ag': 4.15,
    'Cd': 4.50,
    'In': 4.79,
    'Sn': 4.82,
    'Sb': 4.79,
    'Te': 4.83,
    'I':  5.19,
    'Xe': 7.03,
    'Cs': 7.76,
    'Ba': 6.35,
    'La': 5.29,
    'Ce': 4.72,
    'Pr': 4.59,
    'Nd': 4.49,
    'Pm': 4.42,
    'Sm': 4.43,
    'Eu': 4.52,
    'Gd': 4.67,
    'Tb': 4.84,
    'Dy': 4.95,
    'Ho': 5.04,
    'Er': 5.11,
    'Tm': 5.17,
    'Yb': 5.24,
    'Lu': 4.87,
    'Hf': 4.48,
    'Ta': 4.22,
    'W':  4.04,
    'Re': 3.92,
    'Os': 3.86,
    'Ir': 3.86,
    'Pt': 3.97,
    'Au': 4.16,
    'Hg': 5.06,
    'Tl': 4.98,
    'Pb': 5.05,
    'Bi': 5.04,
    'Po': 5.07,
    'At': 5.38,
    'Rn': 7.19,
    'Fr': 7.75,
    'Ra': 6.60,
    'Ac': 5.67,
    'Th': 5.05,
    'Pa': 4.66,
    'U':  4.43,
    'Np': 4.25,
    'Pu': 4.14,
    'Am': 4.11,
    'Cm': 4.12,
    'Bk': 4.17,
    'Cf': 4.30,
    'Es': 4.51,
    'Fm': 4.83,
    'Md': 5.15,
    'No': 5.43,
    }

from ase.calculators.aims import Aims

optimize = False

if len(sys.argv) == 1:
    names = chemical_symbols[1:103]
else:
    names = [sys.argv[1]]

c = ase.db.connect('fcc111.db')

# adsorbate atom height on fcc111 2x2, 4 layers, only atom's coordinates relaxed
# PBE FHI-AIMS light, relativistic atomic_zora scalar
D = {}
D['O'] = {
'H': {'d': 0.97, 'site': 'ontop'},
'He': {'d': 2.95, 'site': 'ontop'},
'Li': {'d': 1.63, 'site': 'ontop'},
'Be': {'d': 1.45, 'site': 'ontop'},
'B': {'d': 1.39, 'site': 'ontop'},
'C': {'d': 1.21, 'site': 'ontop'},
'N': {'d': 1.16, 'site': 'ontop'},
'O': {'d': 1.19, 'site': 'ontop'},
'F': {'d': 1.3, 'site': 'ontop'},
'Ne': {'d': 2.99, 'site': 'ontop'},
'Na': {'d': 2.02, 'site': 'ontop'},
'Mg': {'d': 1.82, 'site': 'ontop'},
'Al': {'d': 1.69, 'site': 'ontop'},
'Si': {'d': 1.6, 'site': 'ontop'},
'P': {'d': 1.53, 'site': 'ontop'},
'S': {'d': 1.49, 'site': 'ontop'},
'Cl': {'d': 1.54, 'site': 'ontop'},
'Ar': {'d': 1.76, 'site': 'ontop'},
'K': {'d': 2.25, 'site': 'ontop'},
'Ca': {'d': 1.93, 'site': 'ontop'},
'Sc': {'d': 1.78, 'site': 'ontop'},
'Ti': {'d': 1.7, 'site': 'ontop'},
'V': {'d': 1.66, 'site': 'ontop'},
'Cr': {'d': 1.64, 'site': 'ontop'},
'Mn': {'d': 1.63, 'site': 'ontop'},
'Fe': {'d': 1.63, 'site': 'ontop'},
'Co': {'d': 1.64, 'site': 'ontop'},
'Ni': {'d': 1.66, 'site': 'ontop'},
'Cu': {'d': 1.73, 'site': 'ontop'},
'Zn': {'d': 1.77, 'site': 'ontop'},
'Ga': {'d': 1.75, 'site': 'ontop'},
'Ge': {'d': 1.72, 'site': 'ontop'},
'As': {'d': 1.69, 'site': 'ontop'},
'Se': {'d': 1.67, 'site': 'ontop'},
'Br': {'d': 1.71, 'site': 'ontop'},
'Kr': {'d': 1.87, 'site': 'ontop'},
'Rb': {'d': 2.34, 'site': 'ontop'},
'Sr': {'d': 2.05, 'site': 'ontop'},
'Y': {'d': 1.91, 'site': 'ontop'},
'Zr': {'d': 1.84, 'site': 'ontop'},
'Nb': {'d': 1.79, 'site': 'ontop'},
'Mo': {'d': 1.76, 'site': 'ontop'},
'Tc': {'d': 1.75, 'site': 'ontop'},
'Ru': {'d': 1.76, 'site': 'ontop'},
'Rh': {'d': 1.78, 'site': 'ontop'},
'Pd': {'d': 1.81, 'site': 'ontop'},
'Ag': {'d': 1.95, 'site': 'ontop'},
'Cd': {'d': 1.98, 'site': 'ontop'},
'In': {'d': 1.97, 'site': 'ontop'},
'Sn': {'d': 1.93, 'site': 'ontop'},
'Sb': {'d': 1.9, 'site': 'ontop'},
'Te': {'d': 1.88, 'site': 'ontop'},
'I': {'d': 1.89, 'site': 'ontop'},
'Xe': {'d': 1.99, 'site': 'ontop'},
'Cs': {'d': 2.23, 'site': 'ontop'},
'Ba': {'d': 2.06, 'site': 'ontop'},
'La': {'d': 1.93, 'site': 'ontop'},
'Ce': {'d': 1.87, 'site': 'ontop'},
'Pr': {'d': 1.85, 'site': 'ontop'},
'Nd': {'d': 1.85, 'site': 'ontop'},
'Pm': {'d': 1.85, 'site': 'ontop'},
'Sm': {'d': 1.85, 'site': 'ontop'},
'Eu': {'d': 1.85, 'site': 'ontop'},
'Gd': {'d': 1.85, 'site': 'ontop'},
'Tb': {'d': 1.86, 'site': 'ontop'},
'Dy': {'d': 1.87, 'site': 'ontop'},
'Ho': {'d': 1.88, 'site': 'ontop'},
'Er': {'d': 1.88, 'site': 'ontop'},
'Tm': {'d': 1.89, 'site': 'ontop'},
'Yb': {'d': 1.91, 'site': 'ontop'},
'Lu': {'d': 1.89, 'site': 'ontop'},
'Hf': {'d': 1.84, 'site': 'ontop'},
'Ta': {'d': 1.8, 'site': 'ontop'},
'W': {'d': 1.78, 'site': 'ontop'},
'Re': {'d': 1.77, 'site': 'ontop'},
'Os': {'d': 1.77, 'site': 'ontop'},
'Ir': {'d': 1.8, 'site': 'ontop'},
'Pt': {'d': 1.84, 'site': 'ontop'},
'Au': {'d': 1.94, 'site': 'ontop'},
'Hg': {'d': 1.94, 'site': 'ontop'},
'Tl': {'d': 2.02, 'site': 'ontop'},
'Pb': {'d': 2.01, 'site': 'ontop'},
'Bi': {'d': 1.98, 'site': 'ontop'},
'Po': {'d': 1.96, 'site': 'ontop'},
'At': {'d': 1.97, 'site': 'ontop'},
'Rn': {'d': 2.02, 'site': 'ontop'},
'Fr': {'d': 2.29, 'site': 'ontop'},
'Ra': {'d': 2.13, 'site': 'ontop'},
'Ac': {'d': 2.02, 'site': 'ontop'},
'Th': {'d': 1.93, 'site': 'ontop'},
'Pa': {'d': 1.88, 'site': 'ontop'},
'U': {'d': 1.85, 'site': 'ontop'},
'Np': {'d': 1.84, 'site': 'ontop'},
'Pu': {'d': 1.84, 'site': 'ontop'},
'Am': {'d': 1.85, 'site': 'ontop'},
'Cm': {'d': 1.85, 'site': 'ontop'},
'Bk': {'d': 1.86, 'site': 'ontop'},
'Cf': {'d': 1.86, 'site': 'ontop'},
'Es': {'d': 1.88, 'site': 'ontop'},
'Fm': {'d': 1.9, 'site': 'ontop'},
'Md': {'d': 1.93, 'site': 'ontop'},
'No': {'d': 1.98, 'site': 'ontop'},
}
D['C'] = {
'H': {'d': 1.12, 'site': 'ontop'},
'He': {'d': 3.06, 'site': 'ontop'},
'Li': {'d': 1.83, 'site': 'ontop'},
'Be': {'d': 1.64, 'site': 'ontop'},
'B': {'d': 1.5, 'site': 'ontop'},
'C': {'d': 1.35, 'site': 'ontop'},
'N': {'d': 1.25, 'site': 'ontop'},
'O': {'d': 1.16, 'site': 'ontop'},
'F': {'d': 1.16, 'site': 'ontop'},
'Ne': {'d': 3.16, 'site': 'ontop'},
'Na': {'d': 2.28, 'site': 'ontop'},
'Mg': {'d': 2.06, 'site': 'ontop'},
'Al': {'d': 1.91, 'site': 'ontop'},
'Si': {'d': 1.8, 'site': 'ontop'},
'P': {'d': 1.69, 'site': 'ontop'},
'S': {'d': 1.59, 'site': 'ontop'},
'Cl': {'d': 1.55, 'site': 'ontop'},
'Ar': {'d': 2.39, 'site': 'ontop'},
'K': {'d': 2.63, 'site': 'ontop'},
'Ca': {'d': 2.18, 'site': 'ontop'},
'Sc': {'d': 1.92, 'site': 'ontop'},
'Ti': {'d': 1.78, 'site': 'ontop'},
'V': {'d': 1.72, 'site': 'ontop'},
'Cr': {'d': 1.68, 'site': 'ontop'},
'Mn': {'d': 1.65, 'site': 'ontop'},
'Fe': {'d': 1.62, 'site': 'ontop'},
'Co': {'d': 1.61, 'site': 'ontop'},
'Ni': {'d': 1.62, 'site': 'ontop'},
'Cu': {'d': 1.74, 'site': 'ontop'},
'Zn': {'d': 1.88, 'site': 'ontop'},
'Ga': {'d': 1.89, 'site': 'ontop'},
'Ge': {'d': 1.86, 'site': 'ontop'},
'As': {'d': 1.82, 'site': 'ontop'},
'Se': {'d': 1.75, 'site': 'ontop'},
'Br': {'d': 1.72, 'site': 'ontop'},
'Kr': {'d': 2.37, 'site': 'ontop'},
'Rb': {'d': 2.76, 'site': 'ontop'},
'Sr': {'d': 2.31, 'site': 'ontop'},
'Y': {'d': 2.06, 'site': 'ontop'},
'Zr': {'d': 1.93, 'site': 'ontop'},
'Nb': {'d': 1.84, 'site': 'ontop'},
'Mo': {'d': 1.8, 'site': 'ontop'},
'Tc': {'d': 1.77, 'site': 'ontop'},
'Ru': {'d': 1.73, 'site': 'ontop'},
'Rh': {'d': 1.71, 'site': 'ontop'},
'Pd': {'d': 1.73, 'site': 'ontop'},
'Ag': {'d': 1.92, 'site': 'ontop'},
'Cd': {'d': 2.1, 'site': 'ontop'},
'In': {'d': 2.11, 'site': 'ontop'},
'Sn': {'d': 2.09, 'site': 'ontop'},
'Sb': {'d': 2.06, 'site': 'ontop'},
'Te': {'d': 1.99, 'site': 'ontop'},
'I': {'d': 1.95, 'site': 'ontop'},
'Xe': {'d': 2.41, 'site': 'ontop'},
'Cs': {'d': 2.74, 'site': 'ontop'},
'Ba': {'d': 2.25, 'site': 'ontop'},
'La': {'d': 2.05, 'site': 'ontop'},
'Ce': {'d': 1.92, 'site': 'ontop'},
'Pr': {'d': 1.87, 'site': 'ontop'},
'Nd': {'d': 1.86, 'site': 'ontop'},
'Pm': {'d': 1.85, 'site': 'ontop'},
'Sm': {'d': 1.85, 'site': 'ontop'},
'Eu': {'d': 1.85, 'site': 'ontop'},
'Gd': {'d': 1.86, 'site': 'ontop'},
'Tb': {'d': 1.89, 'site': 'ontop'},
'Dy': {'d': 1.91, 'site': 'ontop'},
'Ho': {'d': 1.94, 'site': 'ontop'},
'Er': {'d': 1.96, 'site': 'ontop'},
'Tm': {'d': 1.99, 'site': 'ontop'},
'Yb': {'d': 2.04, 'site': 'ontop'},
'Lu': {'d': 2.02, 'site': 'ontop'},
'Hf': {'d': 1.95, 'site': 'ontop'},
'Ta': {'d': 1.9, 'site': 'ontop'},
'W': {'d': 1.87, 'site': 'ontop'},
'Re': {'d': 1.83, 'site': 'ontop'},
'Os': {'d': 1.8, 'site': 'ontop'},
'Ir': {'d': 1.76, 'site': 'ontop'},
'Pt': {'d': 1.76, 'site': 'ontop'},
'Au': {'d': 1.87, 'site': 'ontop'},
'Hg': {'d': 2.05, 'site': 'ontop'},
'Tl': {'d': 2.1, 'site': 'ontop'},
'Pb': {'d': 2.15, 'site': 'ontop'},
'Bi': {'d': 2.15, 'site': 'ontop'},
'Po': {'d': 2.08, 'site': 'ontop'},
'At': {'d': 2.05, 'site': 'ontop'},
'Rn': {'d': 2.42, 'site': 'ontop'},
'Fr': {'d': 2.8, 'site': 'ontop'},
'Ra': {'d': 2.41, 'site': 'ontop'},
'Ac': {'d': 2.2, 'site': 'ontop'},
'Th': {'d': 2.07, 'site': 'ontop'},
'Pa': {'d': 1.97, 'site': 'ontop'},
'U': {'d': 1.91, 'site': 'ontop'},
'Np': {'d': 1.87, 'site': 'ontop'},
'Pu': {'d': 1.85, 'site': 'ontop'},
'Am': {'d': 1.84, 'site': 'ontop'},
'Cm': {'d': 1.82, 'site': 'ontop'},
'Bk': {'d': 1.82, 'site': 'ontop'},
'Cf': {'d': 1.83, 'site': 'ontop'},
'Es': {'d': 1.86, 'site': 'ontop'},
'Fm': {'d': 1.91, 'site': 'ontop'},
'Md': {'d': 2.0, 'site': 'ontop'},
'No': {'d': 2.13, 'site': 'ontop'},
}

# select the basis set
#basis = 'light'
#basis = 'tight'
#basis = 'really_tight'
basis = 'tier2'

kptdensity = 6.0  # this is converged
width = 0.01

charge_mix_param = 0.005
basis_threshold = 0.00001
relativistic = 'none'
relativistic = 1.e-12
relativistic = 'scalar'

sc_accuracy_rho = 1.e-4
sc_accuracy_eev = 5.e-3

code = 'aims' + '-' + basis
code = code + '_k' + str(kptdensity) + '_w' + str(width)
code = code + '_t' + str(basis_threshold) + '_r' + str(relativistic)

for name in D.keys() + names:  # adsorbates + surfaces elements
    for category in ['fcc111', 'fcc']:
        for adsorbate in ['', 'C', 'O']:
            if category == 'fcc111':
                compound = '%s%s-%s' % (name, adsorbate, category)
            else:
                if category == 'fcc' and adsorbate != '':
                    continue
                else:
                    compound = '%s-%s' % (name, category)
            label = compound + '_' + code
            # but here traj file is used as another lock ...
            fd = opencew(label + '.traj')
            if fd is None:
                continue
            traj = PickleTrajectory(label + '.traj', 'w')
            a = fcc[name]
            if category == 'fcc':
                atoms = bulk(name, 'fcc', a=a)
                site = ''
            else:
                atoms = fcc111(name, size=(2, 2, 4), a=a, vacuum=6.0)
                atoms.center(axis=2)
                site = ''
                if adsorbate != '':
                    d = D[adsorbate][name]['d']
                    site = D[adsorbate][name]['site']
                    add_adsorbate(atoms, adsorbate, d, site)
                # relax only adsorbate
                atoms.set_constraint(FixAtoms(mask=atoms.get_tags() >= 1))
            cell = atoms.get_cell()
            kpts = tuple(kpts2mp(atoms, kptdensity, even=True))
            kwargs = {}
            if relativistic == 'scalar':
                kwargs.update({'relativistic': ['atomic_zora', relativistic]})
            elif relativistic == 'none':
                kwargs.update({'relativistic': 'none'})
            else:  # e.g. 1.0e-12
                kwargs.update({'relativistic': ['zora', 'scalar', relativistic]})
            if atoms.get_initial_magnetic_moments().any():  # spin-polarization
                magmom = atoms.get_initial_magnetic_moments().sum() / len(atoms)
                kwargs.update({'spin': 'collinear'})
            if optimize:
                kwargs.update({'sc_accuracy_forces': 1.e-3})
            id = c.reserve(name=name, adsorbate=adsorbate, category=category,
                           site=site,
                           basis=basis,
                           kptdensity=kptdensity, width=width,
                           relativistic=relativistic)
            if id is None:
                continue
            # set calculator
            atoms.calc = Aims(
                label=label,
                species_dir=os.path.join(os.environ['AIMS_SPECIES_DIR'], basis),
                xc='PBE',
                kpts=kpts,
                KS_method='elpa',
                sc_accuracy_rho=sc_accuracy_rho,
                sc_accuracy_eev=sc_accuracy_eev,
                occupation_type=['gaussian', width],
                override_relativity=True,
                override_illconditioning=True,
                basis_threshold=basis_threshold,
                charge_mix_param=charge_mix_param,
                sc_iter_limit=9000,
                )
            atoms.calc.set(**kwargs)  # remaining calc keywords
            if optimize:
                opt = BFGS(atoms, logfile=label + '.opt',
                           trajectory=label + '.traj')
                opt.run(fmax=0.01)
            t = time.time()
            atoms.get_potential_energy()
            c.write(atoms,
                    name=name, adsorbate=adsorbate, category=category,
                    site=site,
                    basis=basis,
                    kptdensity=kptdensity, width=width,
                    relativistic=relativistic,
                    niter=atoms.calc.get_number_of_iterations(),
                    time=time.time()-t)
            traj.write(atoms)
            del c[id]
