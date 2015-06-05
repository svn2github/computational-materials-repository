.. _compression:

Benchmark: compression energies of bulk fcc and rocksalt
========================================================

Reference FHI-AIMS tight basis relativistic atomic_zora scalar
equilibrium volumes compressed/expanded in the range 60% - 150%
of the lattice constant.

* :download:`Download raw data for all codes <compression.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dcompression&
  toggle=user,calculator,name,relativistic>`_

.. contents::
    
Key-value pairs
---------------

===============  =============================================================
key              description
===============  =============================================================
name             Name of the system
relativistic     Non-relativistic and scalar-relativistic results included
project          Name of the project: "compression"
structure        fcc or rocksalt
===============  =============================================================

Note that there are additional keys not explained above which are
specific to the given calculator.


Results
-------

First extract the data of the given code and
insert it into a new database file. Then use the extract.py
and energies.py scripts to write the csv formatted file using the data
from the new database file.

.. literalinclude:: extract.sh

The third step consists of eliminating all
systems that show large scatter of results from the set.
Use the https://svn.fysik.dtu.dk/projects/cmr2/trunk/compression/eliminate.sh script.
This is due to the fact that it is difficult to obtain reliable
results from all-electron codes.
 
The results can be plotted e.g. with https://svn.fysik.dtu.dk/projects/cmr2/trunk/compression/plot.py


Running the calculations again
------------------------------

Selected scripts used to obtain the results are available at
https://svn.fysik.dtu.dk/projects/cmr2/trunk/compression
