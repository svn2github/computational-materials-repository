.. _catapp1:

CatApp database
===============

.. container:: article

    Dr. Jens S. Hummelshøj, Dr. Frank Abild-Pedersen, Dr. Felix Studt,
    Dr. Thomas Bligaard and Prof. Jens K. Nørskov
    
    `CatApp: A Web Application for Surface Chemistry and Heterogeneous
    Catalysis`__
    
    Angewandte Chemie International Edition,
    Volume 51, Issue 1, pages 272–274, January 2, 2012
    
    __ http://dx.doi.org/10.1002/anie.201107947

    
.. contents::
    
The data
--------

* The original :download:`catappdata.csv` file from the `CatApp
  <http://suncat.stanford.edu/theory/outreach/catapp/>`_ web-page
* Download database: :download:`catapp.db`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dcatapp&
  toggle=user,mass,xc,a,b,ab,facet,surface,ea,er>`_
    
The csv-file has been converted to an ASE db-file using this script:
    
.. literalinclude:: csv2db.py


Key-value pairs
---------------

=========  =============================
key        description
=========  =============================
a          Reactant A
b          Reactant B
ab         Product AB
surface    Description of surface
facet      "(111)", "(110)", ...
site       Adsorption site
xc         XC-functional
reference  Reference
url        Link to reference
dataset    Description of calculation
project    Name of the project: "catapp"
=========  =============================


Methane example
---------------

Here we look at the correlation between the activation and reaction energy for this reaction:
    
.. math:: \text{H}* + \text{CH}_3* \rightarrow \text{CH}_4
    
.. literalinclude:: ch4.py

.. image:: ch4.svg
