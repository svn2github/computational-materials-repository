.. _c2dm:

2D Materials
============

This database contains calculated structural and electronic properties of a
range of 2D materials. The database contains the results presented in the following paper:

.. container:: article

    Rasmussen, F., Thygesen, K. S.
    
    `Computational 2D Materials Database: Electronic Structure of Transition-Metal Dichalcogenides and Oxides`__

    J. Phys. Chem. C, 2015, 119 (23), pp 13169–13183, April 30, 2015

    __ http://pubs.acs.org/doi/abs/10.1021/acs.jpcc.5b02950

The data can be downloaded or browsed online as shown below.

* Download raw data: :download:`c2dm.db`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dc2dm&toggle=formula,age,user,calculator,energy,fmax,pbc,volume,charge,mass,magmom,name,xc,hform,a,ind_gap,dir_gap,ind_gap_g0w0,dir_gap_g0w0,magmom,formula&sort%3Dname>`_

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

Examples
--------

The following python script shows how to plot the positions of the VBM and CBM.

.. literalinclude:: plot_band_alignment.py

This produces the figure

.. image:: band_alignment.png

This script plots the LDA and G_0W_0 band structure of MoS2.

.. literalinclude:: plot_band_structure.py

.. image:: H-MoS2_band_structure.png
