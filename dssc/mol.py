# creates: mol.png
from ase.io import read, write
mol = read('dssc.db@M=ZnP,A=EthynPhA,R1=Ph,R2=Ph,R3=Ph')
write('mol.pov', mol, run_povray=True, display=False,
      rotation='140x,-30y,-30z')
