# aims light basis relativistic atomic_zora scalar
ase-db dcdft.db project=dcdft,calculator=aims,basis=light,relativistic=scalar -i dcdft_aims_light.db
python extract.py dcdft_aims_light.db
# aims tight basis relativistic atomic_zora scalar
ase-db dcdft.db project=dcdft,calculator=aims,basis=tight,relativistic=scalar -i dcdft_aims_tight.db
python extract.py dcdft_aims_tight.db
# aims really_tight basis relativistic atomic_zora scalar
ase-db dcdft.db project=dcdft,calculator=aims,basis=really_tight,relativistic=scalar -i dcdft_aims_really_tight.db
python extract.py dcdft_aims_really_tight.db
# aims tier2 basis relativistic atomic_zora scalar
ase-db dcdft.db project=dcdft,calculator=aims,basis=tier2,relativistic=scalar -i dcdft_aims_tier2.db
python extract.py dcdft_aims_tier2.db
# aims tier2 basis relativistic zora scalar 1e-12
ase-db dcdft.db project=dcdft,calculator=aims,basis=tier2,relativistic=1.e-12 -i dcdft_aims_tier2_z12.db
python extract.py dcdft_aims_tier2_z12.db
# aims tier2 basis relativistic none
ase-db dcdft.db project=dcdft,calculator=aims,basis=tier2,relativistic=none -i dcdft_aims_tier2_nrel.db
python extract.py dcdft_aims_tier2_nrel.db
# espresso gbrv 1.2
ase-db dcdft.db project=dcdft,calculator=espresso,potentials=gbrv,potentials_version=1.2 -i dcdft_espresso_gbrv_1.2.db
python extract.py dcdft_espresso_gbrv_1.2.db
# espresso gbrv 1.2
ase-db dcdft.db project=dcdft,calculator=espresso,potentials=gbrv,potentials_version=1.4 -i dcdft_espresso_gbrv_1.4.db
python extract.py dcdft_espresso_gbrv_1.4.db
# espresso sg15_oncv
ase-db dcdft.db project=dcdft,calculator=espresso,potentials=sg15_oncv -i dcdft_espresso_sg15_oncv.db
python extract.py dcdft_espresso_sg15_oncv.db
# abinit gbrv
ase-db dcdft.db project=dcdft,calculator=abinit,potentials=gbrv -i dcdft_abinit_gbrv.db
python extract.py dcdft_abinit_gbrv.db
# abinit hgh
ase-db dcdft.db project=dcdft,calculator=abinit,potentials=hgh -i dcdft_abinit_hgh.db
python extract.py dcdft_abinit_hgh.db
# abinit hgh.sc
ase-db dcdft.db project=dcdft,calculator=abinit,potentials=hgh.sc -i dcdft_abinit_hgh_sc.db
python extract.py dcdft_abinit_hgh_sc.db
# abinit jth
ase-db dcdft.db project=dcdft,calculator=abinit,potentials=jth -i dcdft_abinit_jth.db
python extract.py dcdft_abinit_jth.db
# abinit paw
ase-db dcdft.db project=dcdft,calculator=abinit,potentials=gpaw -i dcdft_abinit_paw09.db
python extract.py dcdft_abinit_paw09.db
# gpaw paw grid spacing 0.10 Angstrom, number of grid points fixed
ase-db dcdft.db project=dcdft,calculator=gpaw,mode=fd,e=0.10,potentials_version=09 -i dcdft_gpaw_fd10_paw09.db
python extract.py dcdft_gpaw_fd10_paw09.db
# gpaw paw grid spacing 0.08 Angstrom, number of grid points fixed
ase-db dcdft.db project=dcdft,calculator=gpaw,mode=fd,e=0.08,potentials_version=09 -i dcdft_gpaw_fd_paw09.db
python extract.py dcdft_gpaw_fd_paw09.db
# gpaw paw planewave cutoff 100 Rydberg, number of grid points and planewaves variable
ase-db dcdft.db project=dcdft,calculator=gpaw,mode=pw,e=1361.0,constant_basis=0,potentials_version=09 -i dcdft_gpaw_pw_variable_paw09.db
python extract.py dcdft_gpaw_pw_variable_paw09.db
# gpaw paw planewave cutoff 100 Rydberg, number of grid points and planewaves fixed
ase-db dcdft.db project=dcdft,calculator=gpaw,mode=pw,e=1361.0,constant_basis=1,potentials_version=09 -i dcdft_gpaw_pw_paw09.db
python extract.py dcdft_gpaw_pw_paw09.db
