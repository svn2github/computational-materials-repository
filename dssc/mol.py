# creates: mol.png
from ase.io import read, write
mol = read('dssc.db@M=Zn,A=EthynPhA,R1=H,R2=H,R3=H')
write('mol.pov', mol, run_povray=True, display=False,
      rotation='140x,-30y,-30z')
