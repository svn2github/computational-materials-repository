# aims tight basis relativistic none
ase-db rocksalt.db project=rocksalt,calculator=aims,basis=tight,relativistic=none -i rocksalt_aims_tight.db
python extract.py rocksalt_aims_tight.db
# aims tier2 basis relativistic none
ase-db rocksalt.db project=rocksalt,calculator=aims,basis=tier2,relativistic=none -i rocksalt_aims_tier2.db
python extract.py rocksalt_aims_tier2.db
