import numpy as np
import matplotlib.pyplot as plt
import ase.db

#function to get and plot E_HOMO and E_LUMO against E_gap for a given metal center and anchor group
def plotter(M, A, c):
    EH = []
    EL = []
    EG = []
    for n in c.select(M=M, A=A): #select dyes with a specific M and A
        kvp = n.key_value_pairs
        EL.append(kvp.E_LUMO)
        EH.append(kvp.E_HOMO)
        EG.append(kvp.E_gap)
    if M=='Zn': #set colors based on metal center
        cl = 'red'
    elif M=='FZn':
        cl = 'gold'
    elif M=='TiO':
        cl = 'magenta'
    elif M=='TiO2R':
        cl = 'pink'
    elif M=='H2':
        cl = 'orange'
    else:
        raise NotImplementedError('Group not defined!')
	
    if A=='EthynPhA': #set symbol based on anchor group
        mk = 's'
    elif A=='2CarboxyPropenA':
        mk = 'o'
    elif A=='2CyanoPropenA':
        mk = '^'
    else:
        raise NotImplementedError('Anchor group not defined!')
	
    plt.plot(EG, EH, color = cl, marker= mk, linestyle='None')
    plt.plot(EG, EL, color = cl, marker= mk, linestyle='None')

#connect to database
c = ase.db.connect('dssc.db') 

#list of metal centers to be plotted
lst = ['Zn', 'TiO', 'H2']

#list of anchor groups to be plotted
ALst = ['EthynPhA', '2CarboxyPropenA', '2CyanoPropenA']

#plot by calling above function
for M in lst:
    for A in ALst:	
        plotter(M, A, c)
    plt.ylabel(r'Energy (eV)', fontsize=18)
    plt.xlabel(r'$E_{\mathrm{gap}}$ (eV)', fontsize=18)
    plt.savefig('HOMO-LUMO.svg')
