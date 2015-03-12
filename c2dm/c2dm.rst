Computational two-dimensional materials
==========================

.. container:: article

    Andersen, K., Latini, S., Thygesen, K. S.
    
    `Dielectric building blocks of van der Waals heterostructures.`__

    (Submitted)

    __ http:/dx.doi.org/


* :download:`Download raw data <file.db>`
* `Browse data <>`_


Key-value pairs
---------------

=====================  =======================================================
key                    description
=====================  =======================================================
name                   Name of 2D material, given byphase and chemical formula. For example 'T-MoS2'

Egap_G0W0              Quasiparticle energy gap 

data                   Dictionary with the dielectric building block of each material

=====================  =======================================================

Keys within data dictionary
---------------

=====================  =======================================================
key                    description
=====================  =======================================================
q                      Grid for parallel momentum transfers

frequencies            Energy grid

chi_monopole           Monopole density response function, array of dimension (q x frequencies)

chi_dipole             Dipole density response function, array of dimension (q x frequencies)

z                      Real space grid perpendicular to the layer

drho_monopole          Monopole induced density, array of dimension  (q x z)

drho_dipole            Dipole induced density, array of dimension (q x z)
=====================  =======================================================


The quantum electrostatic heterostructure (QEH) model
-------------------------------------------------------
The dielectric function of van der waals heterostructures and associated properties can be calculated with the python module, *QEH.py*, that can be downloaded from here: :download:`QEH.py`, and is also available trough GPAW (link and write more)

As an example the macroscopic dielectric function of multilayer MoS2 can be calculated. 
First we extract the data for MoS2: 

.. literalinclude:: multi_MoS2.py
    :lines: 1-19	

Then we use the QEH module to calculate the dielectric function for for one to 20 layers: 

.. literalinclude:: multi_MoS2.py
    :lines: 20-	    

Which should return this result: 

.. image:: epsMoS2.png

The structure is set up with the structure parameter, that should be a list of speciems within the structure. For example a heterostructure of graphene, BN and MoS2 can be defined like: structure=['3H-MoS2', '2BN','graphene', '2BN', '3H-MoS2'], which will give one layer of graphene sandwiched between two layers of hBN and three layers of MoS2 on each side. 
The d parameter should be a list of the distance bewteen all neigboring layers, with a length equal to N-1, where N is the number of layers in the structure. 
