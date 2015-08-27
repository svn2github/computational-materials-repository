# nwchem def2-qzvppd
ase-db g2.db project=g2,calculator=nwchem,basis=def2-qzvppd,relativistic=0,bsse_corrected=0 -i nwchem_def2-qzvppd.nrel.db
python extract.py nwchem nwchem_def2-qzvppd.nrel.db
# nwchem aug-cc-pv5z/aug-cc-pvqz (for Li, Be, Na)
ase-db g2.db project=g2,calculator=nwchem,basis='aug-cc-pv5z/aug-cc-pvqz',relativistic=0,bsse_corrected=0 -i nwchem_aug-cc-pv5z.nrel.db
python extract.py nwchem nwchem_aug-cc-pv5z.nrel.db
# aims tight basis relativistic none
ase-db g2.db project=g2,calculator=aims,basis=tight,relativistic=0,bsse_corrected=0 -i aims_tight.nrel.db
python extract.py aims aims_tight.nrel.db
# aims tight basis relativistic atomic_zora scalar
ase-db g2.db project=g2,calculator=aims,basis=tight,relativistic=atomic_zora -i aims_tight.srel.db
python extract.py aims aims_tight.srel.db
# aims tier2 basis relativistic none
ase-db g2.db project=g2,calculator=aims,basis=tier2,relativistic=0,bsse_corrected=0 -i aims_tier2.nrel.db
python extract.py aims aims_tier2.nrel.db
# aims tier2 basis relativistic atomic_zora scalar
ase-db g2.db project=g2,calculator=aims,basis=tier2,relativistic=atomic_zora -i aims_tier2.srel.db
python extract.py aims aims_tier2.srel.db
# aims tier3 basis relativistic none
ase-db g2.db project=g2,calculator=aims,basis=tier3,relativistic=0,bsse_corrected=0 -i aims_tier3.nrel.db
python extract.py aims aims_tier3.nrel.db
# aims tier3 basis relativistic atomic_zora scalar
ase-db g2.db project=g2,calculator=aims,basis=tier3,relativistic=atomic_zora -i aims_tier3.srel.db
python extract.py aims aims_tier3.srel.db
# aims aug-cc-pVQZ basis relativistic none
ase-db g2.db project=g2,calculator=aims,basis=aug-cc-pVQZ,relativistic=0,bsse_corrected=0 -i aims_aug-cc-pVQZ.nrel.db
python extract.py aims aims_aug-cc-pVQZ.nrel.db
# aims aug-cc-pVQZ basis relativistic atomic_zora scalar
ase-db g2.db project=g2,calculator=aims,basis=aug-cc-pVQZ,relativistic=atomic_zora -i aims_aug-cc-pVQZ.srel.db
python extract.py aims aims_aug-cc-pVQZ.srel.db
# aims aug-cc-pV5Z basis relativistic none
ase-db g2.db project=g2,calculator=aims,basis=aug-cc-pV5Z,relativistic=0,bsse_corrected=0 -i aims_aug-cc-pV5Z.nrel.db
python extract.py aims aims_aug-cc-pV5Z.nrel.db
# aims aug-cc-pV5Z basis relativistic atomic_zora scalar
ase-db g2.db project=g2,calculator=aims,basis=aug-cc-pV5Z,relativistic=atomic_zora -i aims_aug-cc-pV5Z.srel.db
python extract.py aims aims_aug-cc-pV5Z.srel.db
# aims aug-cc-pV6Z basis relativistic none
ase-db g2.db project=g2,calculator=aims,basis=aug-cc-pV6Z,relativistic=0,bsse_corrected=0 -i aims_aug-cc-pV6Z.nrel.db
python extract.py aims aims_aug-cc-pV6Z.nrel.db
# aims aug-cc-pV6Z basis relativistic atomic_zora scalar
ase-db g2.db project=g2,calculator=aims,basis=aug-cc-pV6Z,relativistic=atomic_zora -i aims_aug-cc-pV6Z.srel.db
python extract.py aims aims_aug-cc-pV6Z.srel.db
# aims NAO-VCC-5Z basis relativistic none
ase-db g2.db project=g2,calculator=aims,basis=NAO-VCC-5Z,relativistic=0,bsse_corrected=0 -i aims_NAO-VCC-5Z.nrel.db
python extract.py aims aims_NAO-VCC-5Z.nrel.db
# aims NAO-VCC-5Z basis relativistic atomic_zora scalar
ase-db g2.db project=g2,calculator=aims,basis=NAO-VCC-5Z,relativistic=atomic_zora -i aims_NAO-VCC-5Z.srel.db
python extract.py aims aims_NAO-VCC-5Z.srel.db
# gpaw paw 09 non-relativistic
ase-db g2.db project=g2,calculator=gpaw,potentials_version=0.9,relativistic=0,bsse_corrected=0 -i gpaw_paw09.nrel.db
python extract.py gpaw gpaw_paw09.nrel.db

# nwchem def2-qzvppd bsse corrected
ase-db g2.db project=g2,calculator=nwchem,basis=def2-qzvppd,relativistic=0,bsse_corrected=1 -i nwchem_def2-qzvppd.bsse_corrected.nrel.db
python extract_bsse_corrected.py nwchem nwchem_def2-qzvppd.bsse_corrected.nrel.db
# nwchem aug-cc-pv5z bsse corrected
ase-db g2.db project=g2,calculator=nwchem,basis='aug-cc-pv5z',relativistic=0,bsse_corrected=1 -i nwchem_aug-cc-pv5z.bsse_corrected.nrel.db
python extract_bsse_corrected.py nwchem nwchem_aug-cc-pv5z.bsse_corrected.nrel.db
