# FHI-AIMS light basis relativistic atomic_zora scalar
ase-db dcdft.db calculator=aims,basis=light,relativistic=scalar -i dcdft_aims_light.db
python extract.py dcdft_aims_light.db
# FHI-AIMS tight basis relativistic atomic_zora scalar
ase-db dcdft.db calculator=aims,basis=tight,relativistic=scalar -i dcdft_aims_tight.db
python extract.py dcdft_aims_tight.db
# FHI-AIMS really_tight basis relativistic atomic_zora scalar
ase-db dcdft.db calculator=aims,basis=really_tight,relativistic=scalar -i dcdft_aims_really_tight.db
python extract.py dcdft_aims_really_tight.db
# FHI-AIMS tier2 basis relativistic atomic_zora scalar
ase-db dcdft.db calculator=aims,basis=tier2,relativistic=scalar -i dcdft_aims_tier2.db
python extract.py dcdft_aims_tier2.db
# FHI-AIMS tier2 basis relativistic zora scalar 1e-12
ase-db dcdft.db calculator=aims,basis=tier2,relativistic=1.e-12 -i dcdft_aims_tier2_z12.db
python extract.py dcdft_aims_tier2_z12.db
# FHI-AIMS tier2 basis relativistic none
ase-db dcdft.db calculator=aims,basis=tier2,relativistic=none -i dcdft_aims_tier2_nrel.db
python extract.py dcdft_aims_tier2_nrel.db
# ESPRESSO gbrv
ase-db dcdft.db calculator=espresso,potentials=gbrv -i dcdft_pbe_espresso_gbrv.db
python extract.py dcdft_pbe_espresso_gbrv.db
