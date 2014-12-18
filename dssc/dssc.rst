Porphyrin based dyes
===================================

.. container:: article
  
    Kristian B. Ørnsø, Juan M. García-Lastra and Kristian S. Thygesen

    `Computational screening of functionalized zinc porphyrins for dye
    sensitized solar cells <http://dx.doi.org/10.1039/C3CP54050B>`_

    Phys. Chem. Chem. Phys., 2013, 15, 19478-19486

.. container:: article

    Kristian B. Ørnsø, Christian S. Pedersen, Juan M. García-Lastra and
    Kristian S. Thygesen

    `Optimizing porphyrins for dye sensitized solar cells using large-scale
    ab initio calculations <http://dx.doi.org/10.1039/C4CP01289E>`_

    Phys. Chem. Chem. Phys., 2014, 16, 16246-16254
    

.. contents::
        
* :download:`Download raw data <dssc.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Ddssc>`_


Key-value pairs
---------------

.. figure:: mol.png
    
   Example of dye with: M=Zn, A=EthynPhA, R1=H, R2=H, R3=H

============ ============================================================
key          description
============ ============================================================
M            Metal center
A            Anchor group
R1           First side group
R2           Second side group
R3           Third side group
KS_HOMO      Kohn-Sham HOMO eigenvalue
KS_LUMO      Kohn-Sham LUMO eigenvalue
KS_gap       Kohn-Sham eigenvalue electronic gap (KS_LUMO - KS_HOMO)
E_HOMO       HOMO location calculated as ionization potential
E_LUMO       LUMO location calculated as electron affinity
E_gap        Electronic gap calculated as E_LUMO - E_HOMO
E_c          Energy difference between conduction band and E_HOMO
E_1          Triplet optical gap
E_opt_LUMO   Optical LUMO location calculated as E_HOMO + E_1
LQual1       Level alignment quality calculated with model 1 for the
             open-circuit voltage
LQual2       Level alignment quality calculated with model 2 for the
             open-circuit voltage
project      Name of the project: "dssc"
============ ============================================================


Example of how to use the database to create Figure S1 in the 2014 paper
-------------------------------------------------------------------------

.. include:: homolumo.py
   :start-after: creates
   :code: python

.. image:: homolumo.svg
   :width: 600

