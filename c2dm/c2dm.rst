.. _c2dm:

2D Materials
============

This database contains calculated structural and electronic properties of a
range of 2D materials. The database presently contains the results presented in the two papers:

.. container:: article

    (1) Rasmussen, F., Thygesen, K. S.
    
    `Computational 2D Materials Database: Electronic Structure of Transition
    Metal Dichalcogenides and Oxides`__

    (Submitted)

    __ http:/dx.doi.org/

.. container:: article

    (2) Andersen, K., Latini, S., Thygesen, K. S.
    
    `The Dielectric Genome of van der Waals Heterostructures.`__

    (Submitted)

    __ http:/dx.doi.org/

The data from (1) can be downloaded or browsed online while the data from (2) must be downloaded and used together with e.g. the Python script ``qeh.py`` as shown below.

* Download raw data: :download:`c2dm.db`, :download:`chi-data.tar.gz`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dc2dm&toggle=formula,age,user,calculator,energy,fmax,pbc,volume,charge,mass,name,xc,hform,ind_gap,dir_gap,ind_gap_g0w0,dir_gap_g0w0,formula&sort%3Dname>`_

Electronic structure of 2D materials
------------------------------------

The structures were first relaxed using the PBE xc-functional and a 18x18x1 k-point sampling until all forces on the atoms where below 0.01 eV/Å. The rows with xc='PBE' contains data from these calculations.

For materials that were found to be semiconducting in the PBE calculations we furthermore performed calculations using the LDA and GLLB-SC xc functionals and the lattice constants and atom positions found from the PBE calculation. For these calculations we used a 30x30x1 k-point sampling. For the GLLB-SC calculations we calculated the derivative discontinuity and have added this contribution to the electronic band gaps. Data for these calculations are found in rows with xc='GLLBSC' and xc='LDA', respectively.

Furthermore, we calculated the G0W0 quasiparticle energies using the wavefunctions and eigenvalues from the LDA calculations and a plane-wave cut-off energy of at least 150 eV. The quasiparticle energies where further extrapolated to infinite cut-off energy via the methods described in the paper. The LDA rows thus further have key-value pairs with the results from the G0W0 calculations.


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


Dielectric building blocks
---------------------------

The dielectric building blocks of the materials, that can be used to build van
der Waals heterostructures, is obtained from the file
:download:`chi-data.tar.gz`. This contains a pickle file for each material
with the data described below:

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
