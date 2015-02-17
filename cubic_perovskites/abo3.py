from __future__ import print_function
import ase.db
from ase.phasespace import PhaseSpace

con = ase.db.connect('cubic_perovskites.db')

references = [(row.count_atoms(), row.energy)
              for row in con.select('reference')]

fd = open('abo3.csv', 'w')
print('# id, formula, heat of formation [eV/atom]', file=fd)
for row in con.select(combination='ABO3'):
    count = row.count_atoms()
    refs = []
    for ref in references:
        for symbol in ref[0]:
            if symbol not in count:
                break
        else:
            refs.append(ref)
    ps = PhaseSpace(refs, verbose=False)
    energy = ps.find(**count)[0]
    heat = (row.energy - energy) / row.natoms
    if (heat < 0.21 and
        (3.1 > row.gllbsc_ind_gap > 1.4 or
         3.1 > row.gllbsc_dir_gap > 1.4) and
        (row.VB_ind - 4.5 > 1.23 and row.CB_ind - 4.5 < 0 or
         row.VB_dir - 4.5 > 1.23 and row.CB_dir - 4.5 < 0)):
        formula = row.A_ion + row.B_ion + row.anion
        print('{0}, {1}, {2:.3f}'.format(row.id, formula, heat), file=fd)
