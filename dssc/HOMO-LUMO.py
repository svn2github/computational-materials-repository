import matplotlib.pyplot as plt
import ase.db


def plotter(M, A, c):
    """Function to get and plot E_HOMO and E_LUMO against E_gap for a given
    metal center and anchor group."""
    
    EH = []
    EL = []
    EG = []
    for n in c.select(M=M, A=A):  # select dyes with a specific M and A
        EL.append(n.E_LUMO)
        EH.append(n.E_HOMO)
        EG.append(n.E_gap)
    # Set colors based on metal center:
    cl = {'Zn': 'red',
          'FZn': 'gold',
          'TiO': 'magenta',
          'TiO2R': 'pink',
          'H2': 'orange'}[M]
        
    # Set symbol based on anchor group:
    mk = {'EthynPhA': 's',
          '2CarboxyPropenA': 'o',
          '2CyanoPropenA': '^'}[A]
        
    plt.plot(EG, EH, color=cl, marker=mk, linestyle='None')
    plt.plot(EG, EL, color=cl, marker=mk, linestyle='None')

# Connect to database:
c = ase.db.connect('dssc.db')

# List of metal centers to be plotted:
Mlst = ['Zn', 'TiO', 'H2']

# List of anchor groups to be plotted:
ALst = ['EthynPhA', '2CarboxyPropenA', '2CyanoPropenA']

for M in Mlst:
    for A in ALst:
        plotter(M, A, c)
    plt.ylabel(r'Energy (eV)', fontsize=18)
    plt.xlabel(r'$E_{\mathrm{gap}}$ (eV)', fontsize=18)
    plt.savefig('HOMO-LUMO.svg')
