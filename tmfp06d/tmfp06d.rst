.. _tmfp06d:

The performance of semilocal and hybrid density functionals in 3d transition-metal chemistry 
============================================================================================

Reproducing selected results from
https://dx.doi.org/10.1063/1.2162161 using different codes.

* :download:`Download raw data for all codes <tmfp06d.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dtmfp06d&
  toggle=user,calculator,name,relativistic,xc>`_

.. contents::
    
Key-value pairs
---------------

===============  =============================================================
key              description
===============  =============================================================
name             Name of the system
relativistic     0 or 1
project          Name of the project: "tmfp06d"
xc               Exchange-correlation functional
===============  =============================================================

Note that there are additional keys not explained above which are
specific to the given calculator.


Results
-------

First extract the data of the given code and
insert it into a new database file. Then use the extract.py script
to write the csv formatted file using the data from the new database file.

.. literalinclude:: extract.sh

The systems in this work (many of TM atoms, and TM diatomics) should
not be really treated with GGA DFT for various problems (see for example
http://dx.doi.org/10.1063/1.2723118 or https://dx.doi.org/10.1021/ct2006852).
These problems often translate into convergence problems in various DFT codes
or large scatter of the obtained results.
The third step consists of eliminating all
systems that show large scatter of results from the set.
 
.. literalinclude:: eliminate.sh

The results can be plotted e.g. with:

.. literalinclude:: plot.py


Running the calculations again
------------------------------

Selected scripts used to obtain the results are available at
https://svn.fysik.dtu.dk/projects/cmr2/trunk/tmfp06d
