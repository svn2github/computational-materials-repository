.. _absorption_perovskites:

Absorption spectra of perovskites
=================================

.. container:: article

   Ivano E. Castelli, Kristian S. Thygesen, and Karsten W. Jacobsen
    
    `Calculated optical absorption of different perovskite phases.`__
    
    Journal of Materials Chemistry A, printed online.

    __ http:/dx.doi.org/10.1039/c5ta01586c

* :download:`Download raw data <absorption_perovskites.db>`
* `Browse data
  <http://cmrdb.fysik.dtu.dk/?query=project%3Dabsorption_perovskites&
  toggle=user,calculator,gllbsc_dir_gap,gllbsc_ind_gap,mass,eff>`_


Key-value pairs
---------------

=====================  =======================================================
key                    description
=====================  =======================================================
name                   Name of the structure
phase                  Perovskite phase (cubic, halides_[cubic, tetragonal, orthorhombic], RP, DJ)
gllbsc_dir_gap         Direct bandgap calculated with GLLB-SC
gllbsc_ind_gap         Indirect bandgap calculated with GLLB-SC
gllbsc_disc            Derivative discontinuity calculated with GLLB-SC
project                Name of the project: "absorption_perovskites"
eff                    Calculated efficiency (thickness 1 nm)
eff_max                Calculated efficiency (infinite thickness)
data.energy            Grid used to calculate the Re and Im part of epsilon
data.re_eps            Re(epsilon) in x, y, z direction
data.im_eps            Im(epsilon) in x, y, z direction
=====================  =======================================================


Absorption spectrum of AgNbO3
-----------------------------

.. literalinclude:: spectrum.py

.. image:: spectrum.svg


Calculated efficiencies of the cubic phase perovskites
------------------------------------------------------

This script requires the perfect absorption limit:

* :download:`Download perfect absorption limit <perfect_abs.txt>`

.. literalinclude:: efficiency.py

.. image:: efficiency.svg
