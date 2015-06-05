import os
import shutil
import sys
import time

import numpy as np

import ase.db
from ase.data import atomic_numbers, chemical_symbols, covalent_radii
from ase.io.trajectory import PickleTrajectory
from ase.units import Bohr, Hartree, Rydberg
from ase.utils import opencew
from ase.lattice import bulk
from ase.calculators.calculator import kpts2mp
from ase.parallel import rank, barrier
from ase.calculators.abinit import Abinit
from ase.calculators.aims import Aims
from ase.calculators.elk import ELK
from ase.calculators.exciting import Exciting as ExcitingORIG
# modifications needed to the old-style interfaces
class Exciting(ExcitingORIG):
    name = 'exciting'
    def check_state(self, atoms): return []
    def todict(self): return {}
try:
    from espresso import espresso as espressoORIG
    # modifications needed to the old-style interfaces
    class espresso(espressoORIG):
        name = 'espresso'
        def check_state(self, atoms): return []
        def todict(self): return {}
except ImportError:
    pass
try:
    from ase.calculators.jacapo import Jacapo as JacapoORIG
    # modifications needed to the old-style interfaces
    class Jacapo(JacapoORIG):
        name = 'jacapo'
        def check_state(self, atoms): return []
        def todict(self): return {}
except ImportError:
    pass
from ase.calculators.vasp import Vasp as VaspORIG
# modifications needed to the old-style interfaces
class Vasp(VaspORIG):
    name = 'vasp'
    def check_state(self, atoms): return []
    def todict(self): return {}
from gpaw import GPAW, PW
from gpaw.mixer import Mixer
from gpaw.eigensolvers import Davidson, RMM_DIIS

# shift MP k-points
def get_vkloff(mp):
    vkloff = []  # is this below correct?
    for nk in mp:
        if nk % 2 == 0:  # shift kpoint away from gamma point
            vkloff.append(0.5)
        else:
            vkloff.append(0)
    return ','.join([str(v) for v in vkloff])

# FHI-AIMS PBE tight basis relativistic atomic_zora scalar
lattice_constant = {}
lattice_constant['fcc'] = {
    'H':2.28,
    'He':4.16,
    'Li':4.32,
    'Be':3.15,
    'B':2.87,
    'C':3.08,
    'N':3.12,
    'O':3.17,
    'F':3.43,
    'Ne':4.61,
    'Na':5.32,
    'Mg':4.52,
    'Al':4.04,
    'Si':3.87,
    'P':3.87,
    'S':3.99,
    'Cl':4.39,
    'Ar':5.94,
    'K':6.67,
    'Ca':5.52,
    'Sc':4.62,
    'Ti':4.11,
    'V':3.81,
    'Cr':3.62,
    'Mn':3.5,
    'Fe':3.45,
    'Co':3.45,
    'Ni':3.51,
    'Cu':3.63,
    'Zn':3.93,
    'Ga':4.23,
    'Ge':4.28,
    'As':4.25,
    'Se':4.33,
    'Br':4.72,
    'Kr':6.42,
    'Rb':7.15,
    'Sr':6.02,
    'Y':5.06,
    'Zr':4.52,
    'Nb':4.22,
    'Mo':4.0,
    'Tc':3.87,
    'Ru':3.81,
    'Rh':3.83,
    'Pd':3.94,
    'Ag':4.15,
    'Cd':4.5,
    'In':4.79,
    'Sn':4.82,
    'Sb':4.79,
    'Te':4.83,
    'I':5.19,
    'Xe':7.03,
    'Cs':7.76,
    'Ba':6.35,
    'La':5.29,
    'Ce':4.72,
    'Pr':4.59,
    'Nd':4.49,
    'Pm':4.42,
    'Sm':4.43,
    'Eu':4.52,
    'Gd':4.67,
    'Tb':4.84,
    'Dy':4.95,
    'Ho':5.04,
    'Er':5.11,
    'Tm':5.17,
    'Yb':5.24,
    'Lu':4.87,
    'Hf':4.48,
    'Ta':4.22,
    'W':4.04,
    'Re':3.92,
    'Os':3.86,
    'Ir':3.86,
    'Pt':3.97,
    'Au':4.16,
    'Hg':5.06,
    'Tl':4.98,
    'Pb':5.05,
    'Bi':5.04,
    'Po':5.07,
    'At':5.38,
    'Rn':7.19,
    'Fr':7.75,
    'Ra':6.6,
    'Ac':5.67,
    'Th':5.05,
    'Pa':4.66,
    'U':4.43,
    'Np':4.25,
    'Pu':4.14,
    'Am':4.11,
    'Cm':4.12,
    'Bk':4.17,
    'Cf':4.3,
    'Es':4.51,
    'Fm':4.83,
    'Md':5.15,
    'No':5.43,
}
lattice_constant['rocksalt'] = {
    'H':3.42,
    'He':4.85,
    'Li':4.06,
    'Be':3.65,
    'B':3.89,
    'C':3.97,
    'N':3.94,
    'O':3.99,
    'F':4.22,
    'Ne':5.53,
    'Na':4.8,
    'Mg':4.26,
    'Al':4.48,
    'Si':4.61,
    'P':4.61,
    'S':4.62,
    'Cl':4.76,
    'Ar':5.37,
    'K':5.53,
    'Ca':4.83,
    'Sc':4.47,
    'Ti':4.28,
    'V':4.18,
    'Cr':4.13,
    'Mn':4.1,
    'Fe':4.09,
    'Co':4.1,
    'Ni':4.17,
    'Cu':4.24,
    'Zn':4.33,
    'Ga':4.63,
    'Ge':4.78,
    'As':4.77,
    'Se':4.84,
    'Br':4.99,
    'Kr':5.42,
    'Rb':5.78,
    'Sr':5.2,
    'Y':4.83,
    'Zr':4.6,
    'Nb':4.47,
    'Mo':4.41,
    'Tc':4.39,
    'Ru':4.4,
    'Rh':4.45,
    'Pd':4.53,
    'Ag':4.67,
    'Cd':4.77,
    'In':4.96,
    'Sn':5.13,
    'Sb':5.15,
    'Te':5.2,
    'I':5.35,
    'Xe':5.66,
    'Cs':5.96,
    'Ba':5.59,
    'La':5.15,
    'Ce':4.99,
    'Pr':4.94,
    'Nd':4.9,
    'Pm':4.87,
    'Sm':4.86,
    'Eu':4.84,
    'Gd':4.82,
    'Tb':4.83,
    'Dy':4.83,
    'Ho':4.82,
    'Er':4.81,
    'Tm':4.81,
    'Yb':4.83,
    'Lu':4.74,
    'Hf':4.59,
    'Ta':4.51,
    'W':4.46,
    'Re':4.45,
    'Os':4.48,
    'Ir':4.55,
    'Pt':4.63,
    'Au':4.75,
    'Hg':4.92,
    'Tl':5.11,
    'Pb':5.26,
    'Bi':5.24,
    'Po':5.31,
    'At':5.47,
    'Rn':5.79,
    'Fr':6.04,
    'Ra':5.77,
    'Ac':5.39,
    'Th':5.08,
    'Pa':4.94,
    'U':4.84,
    'Np':4.78,
    'Pu':4.75,
    'Am':4.74,
    'Cm':4.74,
    'Bk':4.77,
    'Cf':4.8,
    'Es':4.84,
    'Fm':4.89,
    'Md':4.94,
    'No':5.02,
}

structures = {}
for s in chemical_symbols[1:103]:
    structures[s] = {'fcc': lattice_constant['fcc'][s], 'rocksalt': lattice_constant['rocksalt'][s]}

# save database into the current directory
c = ase.db.connect(os.path.join(os.getcwd(), 'compression.db'))

code = 'aims'

xc= 'PBE'

if len(sys.argv) == 1:
    elements = chemical_symbols[1:103]
else:
    elements = [sys.argv[1]]

structure = 'fcc'
#structure = 'rocksalt'

kptdensity = 6.0
width = 0.01

charge_mix_param = 0.01
basis_threshold = 0.00001
charge_mix_param = 0.01
sc_accuracy_rho = 1.e-3
sc_accuracy_eev = 5.e-3
sc_accuracy_forces = 5.e-2

if code == 'aims':  # Max occ number of highest state of X for some k-piont is too high!
    charge_mix_param = 0.01
    basis_threshold = 0.00001
    charge_mix_param = 0.01
    sc_accuracy_rho = 1.e-3
    sc_accuracy_eev = 5.e-3
    sc_accuracy_forces = 5.e-2
    if elements[0] in ['La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb',
                       'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
                       'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am',
                       'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No',
    ]:
        width = 0.0001
        basis_threshold = 0.00005
        sc_accuracy_rho = 3.e-3
        sc_accuracy_eev = 5.e-3
        charge_mix_param = 0.005
    if elements[0] in ['Al', 'Mo', 'Tc', 'Ag', 'La', 'Rh',
                       'Pr', 'Nd', 'Pm', 'Eu', 'Gd', 'Tb', 'Dy', 'La', 'Ho', 'Sm']:
        charge_mix_param = 0.005
    if elements[0] in ['Bk', 'Np', 'U', 'Er', 'Ce', 'Tm']:
        charge_mix_param = 0.005
    if elements[0] in ['Pr', 'Nd', 'Pm', 'Rh', 'Eu', 'Gd',
                       'Tb', 'Dy', 'La', 'Ho', 'Ag', 'Sm', 'Pt']:
        charge_mix_param = 0.005
    if elements[0] in ['Dy', 'Ta', 'Re', 'W', 'Os', 'Au', 'Hg']:
        charge_mix_param = 0.0005

if code == 'elk':
    betamax = 0.10
    if len(elements) == 1 and elements[0] in ['C', 'F', 'P', 'Co', 'Ni', 'Ge']:
        betamax = 0.02

    # save ELK_SPECIES_PATH
    ELK_SPECIES_PATH = os.environ.get('ELK_SPECIES_PATH', None)
    assert ELK_SPECIES_PATH is not None

    # DeltaCodesDFT used 2.3 Bohr
    preferred_rmt = 2.00

    # find minimal distances in 70% of lattice constant
    rmt_max = {}
    for name in elements + ['O']:
        if structure == 'rocksalt':
            usename = name + 'O'
        else:
            usename = name
        d = 100.0
        A = bulk(usename, crystalstructure=structure,
                 a=structures[name][structure]).repeat((2,2,2))
        for n1 in range(len(A)):
            for n2 in range(len(A)):
                if n1 != n2 and A.get_distance(n1, n2) < d:
                    d = A.get_distance(n1, n2)
        if d < 100.0:
            # atomic radius * 0.98 - 0.03 Bohr
            rmt_max[name] = min(preferred_rmt, round(d * 0.7 / 2 / Bohr - 0.03, 2))

    # find rmt of the default species
    sfile = os.path.join(os.environ['ELK_SPECIES_PATH'], 'elk.in')
    assert os.path.exists(sfile)
    slines = open(sfile, 'r').readlines()
    rmt_orig = {}
    for name in elements + ['O']:
        found = False
        for n, line in enumerate(slines):
            if line.find("'" + name + "'") > -1:
                begline = n - 1
        for n, line in enumerate(slines[begline:]):
            if not line.strip(): # first empty line
                endline = n
                found = True
                break
        assert found
        # split needed because H is defined with comments
        rmt_orig[name] = float(slines[begline + 3].split()[0].strip())

    # decrease rmt_orig to rmt_max (only if needed)
    rmt = {}
    for name in elements + ['O']:
        if rmt_max[name] < rmt_orig[name]:
            rmt[name] = rmt_max[name]

if code == 'exciting':
    # medium used ~2.0 Bohr
    preferred_rmt = 2.00
    # find minimal distances compressed to 70% of lattice constant
    rmt_max = {}
    for name in elements + ['O']:
        if structure == 'rocksalt':
            usename = name + 'O'
        else:
            usename = name
        d = 100.0
        A = bulk(usename, crystalstructure=structure,
                 a=structures[name][structure]).repeat((2,2,2))
        for n1 in range(len(A)):
            for n2 in range(len(A)):
                if n1 != n2 and A.get_distance(n1, n2) < d:
                    d = A.get_distance(n1, n2)
        if d < 100.0:
            # atomic radius * 0.98 - 0.03 Bohr
            # ase.io.exciting converts Angstrom -> Bohr
            rmt_max[name] = min(preferred_rmt, round(d * 0.7 / 2 / Bohr - 0.03, 2)) * Bohr

    # some default rmt
    rmt_orig = {
        'H': 1.0 * Bohr,
        'He': 1.2 * Bohr,
        'Ne': 1.2 * Bohr,
        # 1.45 default
        'Be': 1.2 * Bohr,
        'B': 1.2 * Bohr,
        'C': 1.2 * Bohr,
        'N': 1.2 * Bohr,
        'O': 1.2 * Bohr,
        'F': 1.2 * Bohr,
        }

    # decrease rmt_orig to rmt_max (only if needed)
    rmt = {}
    for name in elements + ['O']:
        if name not in rmt_orig:
            rmt[name] = rmt_max[name]
        else:
            rmt[name] = rmt_orig[name]

if 0:
    setups = {
        'Ba': '_sv',
        'Ca': '_pv',
        'Ce': '_3',
        'Cs': '_sv',
        'Dy': '_3',
        'Eu': '_3',
        'Fr': '_sv',
        'Gd': '_3',
        'Ho': '_sv',
        'K': '_pv',
        'La': '_s',
        'Lu': '_3',
        'Nb': '_pv',
        'Np': '_s',
        'Pm': '_3',
        'Pr': '_3',
        'Pu': '_s',
        'Ra': '_sv',
        'Rb': '_pv',
        'Sm': '_3',
        'Sr': '_sv',
        'Tb': '_3',
        'Th': '_s',
        'Tm': '_3',
        'U': '_s',
        'Yb': '_2',
        'Y': '_sv',
        'Zr': '_sv',
        # at least those are needed for correct results!
        #'Ti': '_pv',
        #'Ge': '_d',
        #'Re': '_pv',
        #'Os': '_pv',
        }

if 1:  # accurate
    setups = {
        'Ag': '_pv',
        'Al': '_GW',
        'Ar': '_GW',
        'As': '_d',
        'At': '_d',
        'Au': '_pv_GW',
        'B': '_h',
        'Ba': '_sv_GW',
        'Be': '_sv',
        'Bi': '_GW',
        'Br': '_GW',
        'C': '_h',
        'Ca': '_sv',
        'Cd': '_sv_GW',
        'Ce': '_GW',
        'Cl': '_h',
        'Co': '_sv',
        'Cr': '_sv',
        'Cs': '_sv_GW',
        'Cu': '_pv',
        'F': '_h',
        'Fe': '_sv',
        'Fr': '_sv',
        'Ga': '_h',
        'Ge': '_h',
        'H': '_h',
        'Hf': '_sv',
        'In': '_d',
        'K': '_sv',
        'Li': '_sv',
        'Mg': '_sv',
        'Mn': '_sv',
        'Mo': '_sv',
        'N': '_h',
        'Na': '_sv',
        'Nb': '_sv',
        'Ni': '_pv',
        'O': '_h',
        'P': '_h',
        'Pb': '_d',
        'Pd': '_pv',
        'Pt': '_pv',
        'Rb': '_sv',
        'Ra': '_sv',
        'Re': '_pv',
        'Rh': '_pv',
        'Ru': '_sv',
        'S': '_h',
        'Sc': '_sv',
        'Sn': '_d',
        'Sr': '_sv',
        'Ta': '_pv',
        'Ti': '_sv',
        'Tl': '_d',
        'V': '_sv',
        'W': '_pv',
        'Y': '_sv',
        'Zn': '_pv_GW',
        'Zr': '_sv_GW',
        }

parameters = {
    'abinit': {
        'xc':xc,
        'ecut':40*Rydberg,
        'pawecutdg':160*Rydberg,
        'occopt':3,
        'tsmear':width,
        'toldfe':1.0e-6,
        'nstep':400,
        'pawovlp':-1,  # bypass overlap check
        #'diemac':10,
        #'diemix':0.1,
        #'fband':0.75,
        'chksymbreak':0,
    },
    'aims': {
        'xc':xc,
        'species_dir':os.path.join(
            os.environ['AIMS_SPECIES_DIR'], 'tier2'),
        'KS_method':'elpa',
        'sc_accuracy_rho':sc_accuracy_rho,
        'sc_accuracy_eev':sc_accuracy_eev,
        'sc_accuracy_forces':sc_accuracy_forces,
        'basis_threshold':basis_threshold,
        #'relativistic':'atomic_zora,scalar',
        'relativistic':'none',
        'override_relativity':True,
        'occupation_type':'fermi,' + str(width),
        'override_illconditioning':True,
        'charge_mix_param':charge_mix_param,
        'sc_iter_limit':7000,
    },
    'elk': {
        'xc':xc,
        'tasks':0,
        'tforce':True,
        'autokpt':False,
        'swidth':width,
        'rgkmax':8.5,
        'gmaxvr':25,
        'trimvg':False,  # False default
        # http://sourceforge.net/projects/elk/forums/forum/897820/topic/4702970
        'lradstp':1,  # default 4
        # http://sourceforge.net/projects/elk/forums/forum/897820/topic/5089864
        # http://sourceforge.net/projects/elk/forums/forum/897820/topic/5074106
        'lmaxapw':10,  # default 8
        'lmaxvr':7,  # default 7
        'lmaxmat':10,  # very important # default 5
        #'fracinr':0.05,
        'nxapwlo':1,
        'lorbcnd':False,
        #'betamax':betamax,
        'maxscl':1500,
        'autolinengy':False,
        'solscf':1000.0,  # non-relativistic
        'epspot':5.0e-4,
    },
    'exciting': {
        'xctype':'GGA_' + xc,
        'swidth':width / Hartree,
        'rgkmax':8.5,
        'gmaxvr':25,
        'lmaxapw':10,
        'lmaxvr':7,
        'lmaxmat':10, # very important in ELK
        'do':'fromscratch',
        #'fracinr':1.e-12,
        #'SymmetricKineticEnergy':True,
        #'CoreRelativity':'dirac',
        #'ValenceRelativity':'zora',
        'CoreRelativity':'none',
        'ValenceRelativity':'none',
        'useDM':'true',
    },
    'espresso': {
        'xc':xc,
        'pw':100*Rydberg,
        'dw':400*Rydberg,
        'sigma':width,
        'mode':'scf',
        #'verbose':'high',
        #'noncollinear':True,
        #'spinorbit':True,
        'output':{'avoidio':True},  # will overwrite disk_io parameter if True
        'convergence':{'mixing': 0.1, 'maxsteps':500,},
        },
    'gpaw': {
        'xc':xc,
        'mode':PW(80*Rydberg),
        'width':width,
        'idiotproof':False,
        'parallel':{'band':1},
        'maxiter':777,
    },
    'dacapo': {
        'xc':xc,
        'pw':40*Rydberg,
        'dw':50*Rydberg,
        'ft':width,
        'symmetry':True,
        'calculate_stress':False,
        'deletenc':True,
    },
    'vasp': {
        # http://cms.mpi.univie.ac.at/vasp/vasp/vdW_DF_functional_Langreth_Lundqvist_et_al.html
        'xc':xc,
        'encut':80*Rydberg,
        'prec':'high',
        'xc':'PBE',
        'ismear':-1,
        'sigma':width,
        'algo':'Normal',
        'nelm':300,
        'npar':1,
        'lplane':False,
        'lasph':True,
        'addgrid':True,
        'lwave':False,
        'setups': setups,
        'lscalapack':False,
    },
}

linspace = (0.500,0.600,0.700,0.800,0.850,0.900,0.925,0.950,0.975,1.000,1.025,1.050,1.075,1.100,1.125,1.150,1.175,1.200,1.250,1.300,1.350,1.400,1.500)
#linspace = (0.700,0.800,0.850,0.900,0.925,0.950,0.975,1.000,1.025,1.050,1.075,1.100,1.125,1.150,1.175,1.200)

for name in elements:
    # save all steps in one traj file in addition to the database
    # we should only used the database c.reserve, but here
    # traj file is used as another lock ...
    label = code + '_k' + str(kptdensity) + '_w' + str(width)
    fd = opencew(name + '_' + label + '.traj')
    if fd is None:
        continue
    traj = PickleTrajectory(name + '_' + label + '.traj', 'w')
    if name in ['Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']:
        cr = 1.69
    else:
        cr = covalent_radii[atomic_numbers[name]]
    if structure == 'fcc':
        atoms = bulk(name, crystalstructure='fcc',
                     a=structures[name][structure])
        # sum of covelent radii
        scr = cr * 2
    elif structure == 'rocksalt':
        atoms = bulk(name + 'O', crystalstructure='rocksalt',
                     a=structures[name][structure])
        # sum of covelent radii
        scr = cr + covalent_radii[atomic_numbers['O']]
    # calculate the scale factor to recover the distance of scr
    crx = round(scr / atoms.repeat((1,1,2)).get_distance(0, 1), 3)
    kpts = tuple(kpts2mp(atoms, kptdensity, even=True))
    atoms.set_pbc((1,1,1))
    cell = atoms.get_cell()
    if code == 'exciting':
        a = []
        for n, s in enumerate(atoms.get_chemical_symbols()):
            a.append(rmt[s])
        atoms.set_array('rmt', a, float, ())
    # set calculator
    p = parameters[code].copy()
    if code in ['exciting', 'elk']:
        p.update({'autormt': False})
    p.update({'kpts': kpts})
    # loop over EOS linspace
    for n, x in enumerate(linspace):
        id = c.reserve(code=code, name=name, structure=structure,
                       kptdensity=kptdensity, width=width,
                       x=x)
        if id is None:
            continue
        xlabel =  name + '_' + label + '_' + '%02d' % n
        # generate all custom species
        if code == 'elk' and rmt:
            kwargstmp = {}
            atomstmp = atoms.copy()
            if rmt:
                kwargstmp.update({'rmt': rmt})
            os.environ['ELK_SPECIES_PATH'] = ELK_SPECIES_PATH
            atomstmp.calc = ELK(tasks=0, label=xlabel)  # minimal calc
            atomstmp.calc.set(**kwargstmp)  # remaining calc keywords
            atomstmp.get_potential_energy()
            del atomstmp.calc
        # hack ELK_SPECIES_PATH to use custom species
        os.environ['ELK_SPECIES_PATH'] = os.path.abspath(xlabel) + '/'
        # perform EOS step
        atoms.set_cell(cell * x, scale_atoms=True)
        # set calculator
        if code == 'abinit':
            p.update({'label': xlabel})
            calc = Abinit(**p)
        if code == 'aims':
            p.update({'label': xlabel})
            calc = Aims(**p)
        if code == 'elk':
            p.update({'label': xlabel})
            calc = ELK(**p)
        if code == 'exciting':
            p.update({'dir': xlabel})
            p.update({'vkloff': get_vkloff(kpts)})  # k-points shift
            p.update({'speciespath': os.path.join(os.environ['EXCITING_SPECIES_PATH'])})
            p.update({'bin': 'mpiexec ' + os.path.join(os.environ['EXCITINGROOT'], 'bin/excitingmpi')})
            calc = Exciting(**p)
        if code == 'espresso':
            p.update({'outdir': xlabel})
            if not structure.startswith('molecule'):
                p.update({'kptshift': [(nk + 1) % 2 * 1 for nk in kpts]}),
            calc = espresso(**p)
        if code == 'gpaw':
            p.update({'txt': xlabel + '.txt'})
            calc = GPAW(**p)
        if code == 'dacapo':
            p.update({'nc': xlabel + '.nc'})
            calc = Jacapo(**p)
        if code == 'vasp':
            calc = Vasp(**p)
        atoms.calc = calc
        t = time.time()
        e = atoms.get_potential_energy()
        if code in ['dacapo', 'espresso', 'vasp', 'exciting']:
            atoms.calc.results = {'energy': e}
        if code in ['espresso', 'vasp', 'exciting']:
            iter = 0
        else:
            iter=calc.get_number_of_iterations()
        if code == 'vasp':
            os.rename('OUTCAR', xlabel + '.OUTCAR')
            os.rename('INCAR', xlabel + '.INCAR')
            os.rename('POSCAR', xlabel + '.POSCAR')
            os.rename('KPOINTS', xlabel + '.KPOINTS')
        c.write(atoms,
                code=code, name=name, structure=structure,
                kptdensity=kptdensity, width=width,
                x=x,
                iter=iter,
                time=time.time()-t)
        traj.write(atoms)
        del c[id]
