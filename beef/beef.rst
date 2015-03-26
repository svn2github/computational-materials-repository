.. _beef:

Bayesian error estimation functionals
=====================================

.. container:: article

    Jess Wellendorff, Keld T. Lundgaard, Karsten W. Jacobsen, and
    Thomas Bligaard
    
    `mBEEF: An accurate semi-local Bayesian error estimation density
    functional`__
    
    The Journal of Chemical Physics 140, 144107 (2014)
    
    __ http://dx.doi.org/10.1063/1.4870397
    

* :download:`Download raw reference data <beef.db>`
* :download:`Download raw GPAW data <beefgpaw.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dbeef&
  toggle=user,mass,xc,db,ae,ce>`_

.. contents::
    

Key-value pairs
---------------

=======  ===========================================================
key      description
=======  ===========================================================
name     Name of system (molecule, atom, bulk crystal, clean surface
         or surface with adsorbate)
ae       Atomization energy
ce       Chemisorption energy
xc       XC-functional
db       Name of database: "G3/99", "AE6", ...
project  Name of the project: "beef"
=======  ===========================================================


Functionals
-----------

.. literalinclude:: table.py
    :start-after: future

.. csv-table::
    :file: table.csv
    :header-rows: 1

    
Ensembles
---------

Rows with ``xc='mBEEF'`` also contain data for doing ensembles:

.. literalinclude:: ensemble.py
    :start-after: future
    :end-before: output
    
This should print:

.. literalinclude:: output.txt

.. image:: hist.svg

The `8\times 8` mBEEF energy contributions are calculated from
self-consistent mBEEF calculations at mBEEF geometries.


Running the calculations again
------------------------------

This example show how to run all the G3/99 systems with PBE:
    
.. literalinclude:: pbe.py
