# experimental results
python tmfp06d_exp.py

# nwchem def2-qzvppd
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=nwchem,basis=def2-qzvppd,relativistic=0 -i nwchem_def2-qzvppd.nrel.PBE.db
python extract.py nwchem nwchem_def2-qzvppd.nrel.PBE.db
# nwchem aug-cc-pvqz
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=nwchem,basis=aug-cc-pvqz,relativistic=0 -i nwchem_aug-cc-pvqz.nrel.PBE.db
python extract.py nwchem nwchem_aug-cc-pvqz.nrel.PBE.db
# nwchem aug-cc-pv5z
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=nwchem,basis=aug-cc-pv5z,relativistic=0 -i nwchem_aug-cc-pv5z.nrel.PBE.db
python extract.py nwchem nwchem_aug-cc-pv5z.nrel.PBE.db
# aims tight basis relativistic none
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=aims,basis=tight,relativistic=0 -i aims_tight.nrel.PBE.db
python extract.py aims aims_tight.nrel.PBE.db
# aims tier2 basis relativistic none
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=aims,basis=tier2,relativistic=0 -i aims_tier2.nrel.PBE.db
python extract.py aims aims_tier2.nrel.PBE.db
# gpaw paw 09
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=gpaw,potentials_version=09,relativistic=0 -i gpaw_paw09.nrel.PBE.db
python extract.py gpaw gpaw_paw09.nrel.PBE.db

# aims tight basis relativistic atomic_zora scalar
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=aims,basis=tight,relativistic=1 -i aims_tight.srel.PBE.db
python extract.py aims aims_tight.srel.PBE.db
# aims tier2 basis relativistic atomic_zora scalar
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=aims,basis=tier2,relativistic=1 -i aims_tier2.srel.PBE.db
python extract.py aims aims_tier2.srel.PBE.db
# espresso pslib_0.3.1
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=espresso,potentials=pslib,relativistic=1 -i espresso_pslib_0.3.1.srel.PBE.db
python extract.py espresso espresso_pslib_0.3.1.srel.PBE.db
# espresso gbrv 1.2
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=espresso,potentials=gbrv,potentials_version=1.2,relativistic=1 -i espresso_gbrv_1.2.srel.PBE.db
python extract.py espresso espresso_gbrv_1.2.srel.PBE.db
# espresso gbrv 1.4
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=espresso,potentials=gbrv,potentials_version=1.4,relativistic=1 -i espresso_gbrv_1.4.srel.PBE.db
python extract.py espresso espresso_gbrv_1.4.srel.PBE.db
# espresso sg15_oncv
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=espresso,potentials=sg15_oncv,relativistic=1 -i espresso_sg15_oncv.srel.PBE.db
python extract.py espresso espresso_sg15_oncv.srel.PBE.db
# gpaw paw 09
ase-db tmfp06d.db project=tmfp06d,xc=PBE,calculator=gpaw,potentials_version=09,relativistic=1 -i gpaw_paw09.srel.PBE.db
python extract.py gpaw gpaw_paw09.srel.PBE.db
