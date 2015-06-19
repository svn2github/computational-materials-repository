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
    

* Download raw reference data: :download:`molecules.db`, :download:`solids.db`
  and surfaces.db
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dbeef&
  toggle=user,mass,xc,ae,ce,bm,be>`_

.. contents::
    

Key-value pairs
---------------

molecules.db
............
    
=======  ===========================
key      description
=======  ===========================
name     Name of atom or molecule
ae       Atomization energy
xc       XC-functional
project  Name of the project: "beef"
=======  ===========================


solids.db
.........
    
=======  ===========================
key      description
=======  ===========================
name     Name of atom or solid
ce       Cohesive energy
bm       Bulk modulus
xc       XC-functional
project  Name of the project: "beef"
=======  ===========================

Extra data for each row: ``volumes`` and ``energies``.


surfaces.db
...........
    
=======  ===========================
key      description
=======  ===========================
name     Name of atom or solid
be       Binding energy
xc       XC-functional
project  Name of the project: "beef"
=======  ===========================


Performance of functionals
--------------------------

Molecules
.........

.. literalinclude:: table.py
    :start-after: future

Errors in atomization energy (eV):
    
.. csv-table::
    :file: table.csv
    :header-rows: 1


Solids
......

.. literalinclude:: solidstable.py
    :start-after: future

Errors in lattice parameters (%):
    
.. csv-table::
    :file: lp.csv
    :header-rows: 1

Errors in cohesive energies (eV):
    
.. csv-table::
    :file: ce.csv
    :header-rows: 1

Errors in bulk moduli (GPa):
    
.. csv-table::
    :file: bm.csv
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


Reaction energies and error bars
--------------------------------

.. image:: reactions.svg

.. literalinclude:: reactions.py


Running the calculations again
------------------------------

This example show how to run all the molecule systems with PBE:
    
.. literalinclude:: pbe.py
