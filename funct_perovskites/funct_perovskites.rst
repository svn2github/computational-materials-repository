.. _funct_perovskites:

Functional Perovskites
======================

.. container:: article

    Ivano E. Castelli, Mohnish Pandey, Kristian S. Thygesen, and
    Karsten W. Jacobsen

    `Bandgap Engineering of Functional Perovskites Through Quantum
    Confinement and Tunneling`__

    Phys. Rev. B 91, 165309.

    __ http://dx.doi.org/10.1103/PhysRevB.91.165309

* :download:`Download raw data <funct_perovskites.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dfunct_perovskites&
  toggle=user,calculator,comb_A,comb_B,sequence,gllbsc_gamma_gap>`_


Key-value pairs
---------------

==============  =============================================================
key             description
==============  =============================================================
gllbsc_dir_gap  Direct bandgap calculated with GLLB-SC.
gllbsc_ind_gap  Indirect bandgap calculated with GLLB-SC.
gllbsc_disc     Derivative discontinuity calculated with GLLB-SC.
gllbsc_gamma    Bandgap at `\Gamma` calculated with GLLB-SC.
comb_A          Cubic perovskite labeled as A-combination
comb_B          Cubic perovskite labeled as B-combination
sequence        Sequence of A and B layers
project         Name of the project: "funct_perovskites"
==============  =============================================================


Band gaps
---------

Here, we plot the band gaps at `\Gamma` when n A-layers is stuck with
n B-layers (with n between 1 and 6). The changes in the gaps can be
understood in terms of quantum confinement and tunneling. The cubic
perovskites selected as building blocks are BaSnO3 (A) with BaTaO2N (B)
or LaAlO3 (A) with LaTiO2N (B).

.. literalinclude:: figure.py
    
.. image:: gaps.svg
