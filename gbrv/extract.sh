categories='fcc bcc rocksalt perovskite halfheusler'

# aims tier2 basis relativistic atomic_zora scalar
ase-db gbrv.db project=gbrv,calculator=aims,basis=tier2 -i gbrv_aims_tier2.db
for category in $categories;
do
python extract.py gbrv_aims_tier2.db $category
done
# gpaw gpaw 09
ase-db gbrv.db project=gbrv,calculator=gpaw,potentials_version=0.9 -i gbrv_gpaw_paw09.db
for category in $categories;
do
python extract.py gbrv_gpaw_paw09.db $category
done
# espresso sg15_oncv 24Jan2015
ase-db gbrv.db project=gbrv,calculator=espresso,potentials=sg15_oncv,potentials_version=24Jan2015 -i gbrv_espresso_sg15_oncv24Jan2015.db
for category in $categories;
do
python extract.py gbrv_espresso_sg15_oncv24Jan2015.db $category
done
# espresso gbrv 1.2
ase-db gbrv.db project=gbrv,calculator=espresso,potentials=gbrv,potentials_version=1.2 -i gbrv_espresso_gbrv1.2.db
for category in $categories;
do
python extract.py gbrv_espresso_gbrv1.2.db $category
done
# dacapo vanderbilt 2
ase-db gbrv.db project=gbrv,calculator=jacapo,potentials=vanderbilt,potentials_version=2 -i gbrv_dacapo_vanderbilt2.db
for category in $categories;
do
python extract.py gbrv_dacapo_vanderbilt2.db $category
done

# exciting iora*
categories='fcc bcc rocksalt'
ase-db gbrv.db project=gbrv,calculator=exciting -i gbrv_exciting.db
for category in $categories;
do
python extract.py gbrv_exciting.db $category
done

