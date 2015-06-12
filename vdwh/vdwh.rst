.. _vdwh:

Van der Waals heterostructures
==============================

This database contains the dielectric building blocks of 51 transition metal dichalcogenides and oxides, hexagonal boron nitride, and graphene at ten different doping levels. These results are used to calculate the dielectric function of van der Waals heterostructures that is build as combinations of these materials.  The following article has been submitted for publication:

.. container:: article

    Andersen, K., Latini, S., Thygesen, K. S.
    
    `Dielectric Genome of van der Waals Heterostructures.`__

    Nano Letters (2015)
    
    __ http:/dx.doi.org/10.1021/acs.nanolett.5b01251

The data can be downloaded and used together with e.g. the Python script ``qeh.py`` as shown below. The dielectric building blocks are obtained from the file:

* Download raw data :download:`chi-data.tar.gz`

The electronic band gap and band edge positions of the trantision metal dichalcogenides and oxides are available from the 2D materials database :ref:`c2dm`, where both metallic and semiconducting materials have been studied. These results can be browsed online with the link:

* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dc2dm&toggle=formula,age,user,calculator,energy,fmax,pbc,volume,charge,mass,name,xc,hform,ind_gap,dir_gap,ind_gap_g0w0,dir_gap_g0w0,formula&sort%3Dname>`_

The dielelectric building blocks have presently only been calculated for the 51 semiconducing materials found to be stable in the study above.

Dielectric building blocks
---------------------------

As explained above, the dielectric building blocks of the materials are obtained from the file :download:`chi-data.tar.gz`. This contains a pickle file for each material called: *<name>-chi.pckl*, where the name consists of the phase (*'H'* for 2H and *'T'* for 1T) followed by the chemical formula, such that the file for 2H-MoS2 is called: *H-MoS2-chi.pckl*. The files contain the data described in the table below:

=====================  =======================================================
quantity                  description
=====================  =======================================================
q                      Grid for parallel momentum transfers

frequencies            frequency grid

chi_monopole           Monopole density response function, array of dimension
                       (q x frequencies)

chi_dipole             Dipole density response function, array of dimension
                       (q x frequencies)

z                      Real space grid perpendicular to the layer

drho_monopole          Monopole induced density, array of dimension  (q x z)

drho_dipole            Dipole induced density, array of dimension (q x z)
=====================  =======================================================


The quantum electrostatic heterostructure (QEH) model
-----------------------------------------------------

The dielectric function of van der waals heterostructures and associated
properties can be calculated with the python module in the script, *qeh.py*,
that can be downloaded from here: :download:`qeh.py`, and is also available
trough GPAW. 

As an example the macroscopic dielectric function of multilayer MoS2 can be
obtained. First we extract the data for MoS2 from the database::

    $ tar xf chi-data.tar.gz
    $ cp chi-data/H-MoS2-chi.pckl .
    
Then the Heterostructure module is used to calculate the dielectric function
for one to 20 layers of MoS2.

.. literalinclude:: multi_MoS2.py
    :start-after: Calculate

Which should return this result:

.. image:: epsMoS2.svg

The structure is set up with the structure parameter, that should be a list of
speciems within the structure. In this case ``structure=['20MoS2']`` gives 20
layers of MoS2. As an example a more complicated heterostructure of graphene,
hBN and MoS2 can be set up with: ``structure=['3H-MoS2', '2BN','graphene',
'2BN', '3H-MoS2']``, which will give one layer of graphene sandwiched between
two layers of hBN and three layers of MoS2 on each side. The d parameter
should be a list of the distance bewteen all neigboring layers, with a length
equal to N-1, where N is the number of layers in the structure.
