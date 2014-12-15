Bayesian error estimation functionals
=====================================

.. container:: article

    ...

* :download:`Download raw data <beef.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dbeef>`_


Key-value pairs
---------------

=======  ===========================
key      description
=======  ===========================
name     Name of molecule/atom
ae       Atomization energy
xc       XC-functional
db       Name of database: "G3/99"
project  Name of the project: "beef"
=======  ===========================


Functionals
-----------

.. literalinclude:: table.py

.. csv-table::
    :file: table.csv
    :header-rows: 1

    
Ensembles
---------

The rows with ``xc='mBEEF'`` also contain data for doing ensembles:

.. literalinclude:: ensemble.py
    :start-after: future
    :end-before: output
    
This should print:

.. literalinclude:: output.txt

.. image:: hist.svg
