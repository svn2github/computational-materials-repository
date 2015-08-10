.. _gbrv:

Pseudopotentials for high-throughput DFT calculations
=====================================================

Reproducing results from
http://dx.doi.org/10.1016/j.commatsci.2013.08.053 using different codes.

* :download:`Download raw data for all codes <gbrv.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dgbrv&
  toggle=user,calculator,category,name>`_

.. contents::
    
Key-value pairs
---------------

===========  =====================================================================
category     One of: fcc, bcc, rocksalt, perovskite, halfheulser, magnetic_moments
kptdensity   K-point density in point per Ang^-1
linspacestr  Numpy's linspace used for scaling the cell along the EOS
name         Name of the compound
project      Name of the project: "gbrv"
width        Electronic temperature
x            Strain used to scale the cell along the EOS (see linspacestr)
===========  =====================================================================

Note that there are additional keys not explained above which are
specific to the given calculator.


Results
-------

First extract the data of the given code and
insert it into a new database file. Then use the extract.py script
to write the csv formatted file using the data from the new database file.
In addition to the csv file a corresponding txt file is created.

.. literalinclude:: extract.sh

Then use the https://svn.fysik.dtu.dk/projects/cmr2/trunk/gbrv/gbrvDelta.py
to calculate the Delta factors, e.g.::

   python gbrvDelta.py gbrv_aims_tier2.db_fcc_raw.txt gbrv_espresso_gbrv1.2.db_fcc_raw.txt -s

**Note**: the WIEN2k/VASP results published in http://dx.doi.org/10.1016/j.commatsci.2013.08.053
can be extracted using the https://svn.fysik.dtu.dk/projects/cmr2/trunk/gbrv/gbrv_doi.py script.

Running the calculations again
------------------------------

Selected scripts used to obtain the results are available at
https://svn.fysik.dtu.dk/projects/cmr2/trunk/gbrv
