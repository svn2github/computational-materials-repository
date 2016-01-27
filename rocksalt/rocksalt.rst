.. _rocksalt:

Rocksalt equation of state
==========================

The results are PBE, non-relativistic, calculated on FHI-AIMS tight
basis, relativistic atomic_zora scalar PBE reference lattice constants.
The reference lattice constants were rounded to 0.01 Angstrom.

* :download:`Download raw data for all codes <rocksalt.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Drocksalt&
  toggle=user,calculator,name,relativistic>`_

.. contents::
    
Key-value pairs
---------------

===========  ===========================================
key              description
===========  ===========================================
kptdensity   K-point density in point per Ang^-1
name         Name of the compound
project      Name of the project: "rocksalt"
width        Electronic temperature
x            Strain used to scale the cell along the EOS
===========  ===========================================

Note that there are additional keys not explained above which are
specific to the given calculator.


Results
-------

First extract the data of the given code and
insert it into a new database file. Then use the extract.py script
to write the csv formatted file using the data from the new database file.
In addition to the csv file a corresponding txt file is created.

.. literalinclude:: extract.sh

**Note**: it takes a long time (hours). There are ~3500 compounds
per calculator for which calculation of EOS parameters takes place.

Then use the https://svn.fysik.dtu.dk/projects/cmr2/trunk/rocksalt/rocksaltDelta.py
to calculate the Delta factors, e.g.::

   python rocksaltDelta.py rocksalt_aims_tight.db_raw.txt rocksalt_aims_tier2.db_raw.txt -s

**Note** that many "exotic" binary systems fail to converge or obtain a smooth equation of state.
This is more prevalent for the "tight" rather than "tier2" FHI-AIMS basis set.
Most of such systems have been removed from the database, but some obtained using 
the "tight" basis set left as an example (e.g. AcFr).


Running the calculations again
------------------------------

Selected scripts used to obtain the results are available at
https://svn.fysik.dtu.dk/projects/cmr2/trunk/rocksalt
