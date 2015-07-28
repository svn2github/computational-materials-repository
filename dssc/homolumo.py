# creates: homolumo.svg
import matplotlib.pyplot as plt
import ase.db


def plotter(M, A, c):
    """Function to get and plot E_HOMO and E_LUMO against E_gap for a given
    metal center and anchor group."""
    
    EH = []
    EL = []
    EG = []
    for row in c.select(M=M, A=A):  # select dyes with a specific M and A
        EL.append(row.E_LUMO)
        EH.append(row.E_HOMO)
        EG.append(row.E_gap)
    # Set colors based on metal center:
    cl = {'ZnP': 'red',
          'FZnP': 'gold',
          'TiOP': 'magenta',
          'FTiOP': 'purple',
          'TiO2RP': 'pink',
          'FTiO2RP': 'cadetblue',
          'H2P': 'orange',
          'FH2P': 'coral'}[M]
        
    # Set symbol based on anchor group:
    mk = {'EthynPhA': 's',
          '2CarboxyPropenA': 'o',
          '2CyanoPropenA': '^',
	  'EthenThPCyanoAcryl': 'v',
	  'DThPCyanoAcryl': '<',
	  'EthynDThPA': '>',
	  'EthynBTDPhA': '8',
	  'EthynPhM': 'p',
	  'EthynThPA': '*',
	  'EthynDPhEPhA': 'h',
	  'EthynThPCyanoAcryl': '+',
	  'EthynPhEPhA': 'x',
	  'EthynDThPCyanoAcryl': 'd',
	  'EthynFuA': 'D',
	  'ThPCyanoAcryl': 'H',
	  'EthynTPhEPhA': '1',
	  'EthenCyanoAcryl': '2',
          'EthynPhDA': '3'}[A]
        
    plt.plot(EG, EH, color=cl, marker=mk, linestyle='None')
    plt.plot(EG, EL, color=cl, marker=mk, linestyle='None')

c = ase.db.connect('dssc.db')

for M in ['ZnP', 'TiOP', 'H2P']:  # metal centers
    for A in ['EthynPhA', '2CarboxyPropenA', '2CyanoPropenA']:  # anchor groups
        plotter(M, A, c)
    plt.ylabel(r'Energy (eV)', fontsize=18)
    plt.xlabel(r'$E_{\mathrm{gap}}$ (eV)', fontsize=18)
    plt.savefig('homolumo.svg')
