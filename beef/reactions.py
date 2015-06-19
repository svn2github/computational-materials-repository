# creates: reactions.svg
import numpy as np
import matplotlib.pyplot as plt
import ase.db
from ase.dft.bee import ensemble

re42 = (
    'C2H2+H2->C2H4, CH4+CO2->2CO+2H2, 3O2->2O3, CO2+3H2->CH3OH+H2O, '
    '2CH3OH+O2->2CO2+4H2, 4CO+9H2->trans-butane+4H2O, CH3CH2OH->CH3OCH3, '
    'CO+H2O->CO2+H2, C3H6_Cs+H2->C3H8, Cyclohexadiene_1_4+2H2->Cyclohexane, '
    'isobutane->trans-butane, 2CO+2NO->2CO2+N2, CH4+2Cl2->CCl4+2H2, '
    '2N2+O2->2N2O, H2+O2->H2O2, N2+2H2->N2H4, N2+2O2->2NO2, '
    'CH2OCH2+H2->C2H4+H2O, CO+2H2->CH3OH, C3H4_D2d+2H2->C3H8, O2+2H2->2H2O, '
    'N2+3H2->2NH3, CH4+2F2->CF4+2H2, H2CCO+2H2->C2H4+H2O, N2+O2->2NO, '
    'O2+4HCl->2Cl2+2H2O, CO2+4H2->CH4+2H2O, '
    'Cyclohexadiene_1_3->Cyclohexadiene_1_4, CO+3H2->CH4+H2O, '
    'CH4+CO2->CH3COOH, CH4+NH3->HCN+3H2, 2CO+O2->2CO2, C3H4_C3v+H2->C3H6_Cs, '
    'CO+H2O->HCOOH, H3CNH2+H2->CH4+NH3, O2+H2->2OH, '
    'C6H6+H2->Cyclohexadiene_1_4, CH4+H2O->CH3OH+H2, CH4+CO+H2->CH3CH2OH, '
    'CH3CH2SH+H2->SH2+C2H6, SO2+3H2->SH2+2H2O, 2OH+H2->2H2O').split(', ')

reactions = []
for name in re42:
    reaction = []
    sign = 1
    for formula in name.split('->'):
        for mol in formula.split('+'):
            if mol[0].isdigit():
                n = int(mol[0])
                mol = mol[1:]
            else:
                n = 1
            reaction.append((sign * n, mol))
        sign = -1
    reactions.append((name, reaction))

con = ase.db.connect('molecules.db')
errors = []
errorbars = []
for name, reaction in reactions:
    Eref = 0.0
    E = 0.0
    dE = 0.0
    for n, mol in reaction:
        rowref = con.get(name=mol, calculator='exp')
        Eref += n * rowref.energy
        row = con.get(name=mol, xc='mBEEF')
        E += n * row.energy
        dE += n * ensemble(row.energy, row.data.contributions, 'mBEEF')
    errors.append(E - Eref)
    errorbars.append(dE.std())

fig = plt.figure()
ax = fig.add_subplot(111)
x = 1 + np.arange(len(errors))
ax.errorbar(x, errors, yerr=errorbars, fmt='o')
ax.plot(x, 0 * x, '-')
ax.set_xlabel('Reaction #')
ax.set_ylabel('Reaction energy error (eV)')
plt.savefig('reactions.svg')
