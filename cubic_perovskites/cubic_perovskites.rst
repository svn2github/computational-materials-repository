.. _cubic_perovskites:

Perovskite water-splitting
==========================

.. container:: article

    Castelli, I. E., Landis, D. D., Thygesen, K. S., Dahl, S.,
    Chorkendorff, I., Jaramillo, T. F., and Jacobsen, K. W.
    
    `New cubic perovskites for one- and two-photon water splitting using the
    computational materials repository.`__
    
    Energy Environ. Sci. 5, 9034.

    __ http:/dx.doi.org/10.1039/C2EE22341D

.. container:: article

    Castelli, I. E., Olsen, T., Datta, S., Landis, D. D., Dahl, S.,
    Thygesen, K. S., and Jacobsen, K. W.
    
    `Computational screening of perovskite metal oxides for optimal solar
    light capture.`__
    
    Energy Environ. Sci. 5, 5814.

    __ http:/dx.doi.org/10.1039/C1EE02717D

.. container:: article

    Castelli, I. E., Thygesen, K. S., and Jacobsen, K. W.

    `Calculated Pourbaix Diagrams of Cubic Perovskites for Water
    Splitting: Stability Against Corrosion.`__

    Topics in Catalysis 57, 265.

    __ http:/dx.doi.org/10.1007/s11244-013-0181-4

* :download:`Download raw data <cubic_perovskites.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dcubic_perovskites&
  toggle=user,calculator,gllbsc_dir_gap,gllbsc_ind_gap,mass,
  heat_of_formation_all>`_


Key-value pairs
---------------

=====================  =======================================================
key                    description
=====================  =======================================================
A_ion                  A-ion in the cubic perovskite
B_ion                  B-ion in the cubic perovskite
anion                  Anion combination in the perovskite
gllbsc_dir_gap         Direct bandgap calculated with GLLB-SC
gllbsc_ind_gap         Indirect bandgap calculated with GLLB-SC
heat_of_formation_all  Heat of formation calculated with respect to all
                       the materials in the pool of references
project                Name of the project: "cubic_perovskites"
combination            General formula
CB_dir, CB_ind         Direct and Indirect position of the conduction band
                       edge
VB_dir, VB_ind         Indirect and Indirect position of the conduction band
                       edge
reference              "standard" (used to calculate the standard
                       heat of formation) or "pool" (reference included in
                       the calculation of the convex hull)
=====================  =======================================================


ABO3 candidates for water splitting
-----------------------------------

.. literalinclude:: abo3.py

The 10 candidates are:
    
.. csv-table::
    :file: abo3.csv
    :header-rows: 1

Here are the band gaps:
    
.. image:: abo3.svg

.. literalinclude:: abo3fig.py

The stability of a material with respect to solid and dissolved phases
can be evaluated using Pourbaix diagrams. Here how to generate the
Pourbaix diagram for SrTiO3:

.. literalinclude:: SrTiO3_pourbaix.py

.. image:: SrTiO3_pourbaix.png

Here how to plot the energy differences for all (oxides: 10,
oxynitrides: 7, oxyfluorides: 3) the candidate material and the most
stable experimental known solid and dissolved phases at pH = 7 and for
a potential between -1 and 2 V:

.. literalinclude:: candidates_pourbaix.py

.. image:: WS_pourbaix.png
