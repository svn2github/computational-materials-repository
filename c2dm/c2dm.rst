.. _c2dm:

2D Materials
============

.. container:: article

    Rasmussen, F., Thygesen, K. S.
    
    `Computational 2D Materials Database: Electronic Structure of Transition
    Metal Dichalcogenides and Oxides`__

    (Submitted)

    __ http:/dx.doi.org/

.. container:: article

    Andersen, K., Latini, S., Thygesen, K. S.
    
    `The Dielectric Genome of van der Waals Heterostructures.`__

    (Submitted)

    __ http:/dx.doi.org/


* Download raw data: :download:`c2dm.db`, :download:`chi-data.tar.gz`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dc2dm&toggle=name>`_

This database contains calculated structural and electronic properties of a
range of 2D materials.


Key-value pairs
---------------

=====================  =======================================================
key                    description
=====================  =======================================================
name                   Name or chemical formula of the material
phase                  Designation of the phase of the material, either 'H' or
                       'T'
xc                     Exchange-correlation functional used
hform                  Heat of formation
hform_fere             Heat of formation based on fitted elemental
                       phase reference energies
ind_gap                DFT indirect band gap
dir_gap                DFT direct band gap
vbm                    DFT valence band maximum relative to vacuum
cbm                    DFT conduction band minimum relative to vacuum
ind_gap_g0w0           G0W0 indirect band gap
dir_gap_g0w0           G0W0 direct band gap
vbm_g0w0               G0W0 valence band maximum
cbm_g0w0               G0W0 conduction band minimum
emass1_g0w0            G0W0 electron mass (direction 1 - smallest)
emass2_g0w0            G0W0 electron mass (direction 2 - largest)
hmass1_g0w0            G0W0 hole mass (direction 1 - smallest)
hmass2_g0w0            G0W0 hole mass (direction 2 - largest)
q2d_macro_df_slope     Slope of macroscopic 2D static dielectric function at
                       q=0
=====================  =======================================================

The dielectric building blocks of the materials, that can be used to build van
der Waals heterostructures, is obtained from the file
:download:`chi-data.tar.gz`. This contains a pickle file for each material
with the data described below:


Dielectric building blocks
---------------------------

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
