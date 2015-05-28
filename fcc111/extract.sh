# aims light basis relativistic atomic_zora scalar
ase-db fcc111.db project=fcc111,calculator=aims,basis=light,relativistic=scalar -i fcc111_aims_light.db
python extract.py fcc111_aims_light.db
# aims tight basis relativistic atomic_zora scalar
ase-db fcc111.db project=fcc111,calculator=aims,basis=tight,relativistic=scalar -i fcc111_aims_tight.db
python extract.py fcc111_aims_tight.db
# aims tier2 basis relativistic atomic_zora scalar
ase-db fcc111.db project=fcc111,calculator=aims,basis=tier2,relativistic=scalar -i fcc111_aims_tier2.db
python extract.py fcc111_aims_tier2.db
# espresso gbrv 1.2
ase-db fcc111.db project=fcc111,calculator=espresso,potentials=gbrv,potentials_version=1.2,relativistic=scalar -i fcc111_espresso_gbrv1.2.db
python extract.py fcc111_espresso_gbrv1.2.db
# espresso pslib 0.3.1
ase-db fcc111.db project=fcc111,calculator=espresso,potentials=pslib,potentials_version=0.3.1,relativistic=scalar -i fcc111_espresso_pslib0.3.1.db
python extract.py fcc111_espresso_pslib0.3.1.db
# espresso sg15_oncv 24Jan2015
ase-db fcc111.db project=fcc111,calculator=espresso,potentials=sg15_oncv,potentials_version=24Jan2015,relativistic=scalar -i fcc111_espresso_sg15_oncv24Jan2015.db
python extract.py fcc111_espresso_sg15_oncv24Jan2015.db
# dacapo vanderbilt 2
ase-db fcc111.db project=fcc111,calculator=dacapo,potentials=vanderbilt,potentials_version=2,relativistic=scalar -i fcc111_dacapo_vanderbilt2.db
python extract.py fcc111_dacapo_vanderbilt2.db
# gpaw gpaw 08
ase-db fcc111.db project=fcc111,calculator=gpaw,potentials=gpaw,potentials_version=0.8,relativistic=scalar -i fcc111_gpaw_gpaw08.db
python extract.py fcc111_gpaw_gpaw08.db
# gpaw gpaw 09
ase-db fcc111.db project=fcc111,calculator=gpaw,potentials=gpaw,potentials_version=0.9,relativistic=scalar -i fcc111_gpaw_gpaw09.db
python extract.py fcc111_gpaw_gpaw09.db
