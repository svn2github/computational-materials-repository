# rocksalt aims tier2 basis relativistic none
ase-db compression.db project=compression,structure=rocksalt,calculator=aims,basis=tier2,relativistic=0 -i rocksalt.aims_tier2.nrel.db
python extract.py rocksalt.aims_tier2.nrel.db
python energies.py rocksalt.aims_tier2.nrel.db
# aims tier2 basis relativistic none
ase-db compression.db project=compression,structure=fcc,calculator=aims,basis=tier2,relativistic=0 -i fcc.aims_tier2.nrel.db
python extract.py fcc.aims_tier2.nrel.db
python energies.py fcc.aims_tier2.nrel.db
# aims tier2 basis relativistic atomic_zora scalar
ase-db compression.db project=compression,structure=fcc,calculator=aims,basis=tier2,relativistic=atomic_zora -i fcc.aims_tier2.srel.db
python extract.py fcc.aims_tier2.srel.db
python energies.py fcc.aims_tier2.srel.db
# elk nrel
ase-db compression.db project=compression,structure=fcc,calculator=elk,relativistic=0 -i fcc.elk.nrel.db
python extract.py fcc.elk.nrel.db
python energies.py fcc.elk.nrel.db
# elk srel
ase-db compression.db project=compression,structure=fcc,calculator=elk,relativistic=scalar -i fcc.elk.srel.db
python extract.py fcc.elk.srel.db
python energies.py fcc.elk.srel.db
# rocksalt exciting nrel
ase-db compression.db project=compression,structure=rocksalt,calculator=exciting,relativistic=0 -i rocksalt.exciting.nrel.db
python extract.py rocksalt.exciting.nrel.db
python energies.py rocksalt.exciting.nrel.db
# exciting nrel
ase-db compression.db project=compression,structure=fcc,calculator=exciting,relativistic=0 -i fcc.exciting.nrel.db
python extract.py fcc.exciting.nrel.db
python energies.py fcc.exciting.nrel.db
# exciting zora
ase-db compression.db project=compression,structure=fcc,calculator=exciting,relativistic=zora -i fcc.exciting.zora.db
python extract.py fcc.exciting.zora.db
python energies.py fcc.exciting.zora.db
# exciting iora*
ase-db compression.db project=compression,structure=fcc,calculator=exciting,relativistic='iora*' -i 'fcc.exciting.iora*.db'
python extract.py 'fcc.exciting.iora*.db'
python energies.py 'fcc.exciting.iora*.db'
# gpaw paw 09 nrel
ase-db compression.db project=compression,structure=fcc,calculator=gpaw,potentials_version=9.,relativistic=0 -i fcc.gpaw_paw09.nrel.db
python extract.py fcc.gpaw_paw09.nrel.db
python energies.py fcc.gpaw_paw09.nrel.db
# espresso gbrv 1.4
ase-db compression.db project=compression,structure=fcc,calculator=espresso,potentials=gbrv,potentials_version=1.4,relativistic=scalar -i fcc.espresso_gbrv_1.4.srel.db
python extract.py fcc.espresso_gbrv_1.4.srel.db
python energies.py fcc.espresso_gbrv_1.4.srel.db
# espresso sg15_oncv
ase-db compression.db project=compression,structure=fcc,calculator=espresso,potentials=sg15_oncv,potentials_version=20May2015,relativistic=scalar -i fcc.espresso_sg15_oncv.srel.db
python extract.py fcc.espresso_sg15_oncv.srel.db
python energies.py fcc.espresso_sg15_oncv.srel.db
# espresso sssp accurate 0.6
ase-db compression.db project=compression,structure=fcc,calculator=espresso,potentials=sssp_accurate,potentials_version=0.6,relativistic=scalar -i fcc.espresso_sssp_accurate.srel.db
python extract.py fcc.espresso_sssp_accurate.srel.db
python energies.py fcc.espresso_sssp_accurate.srel.db
