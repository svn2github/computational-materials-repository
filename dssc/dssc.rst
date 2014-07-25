Data for zinc porphyrins based dyes
===================================

.. container:: article
  
    Kristian B. Ørnsø, Juan M. García-Lastra and Kristian S. Thygesen

    `Computational screening of functionalized zinc porphyrins for dye
    sensitized solar cells`__

    Phys. Chem. Chem. Phys., 2013,15, 19478-19486

    __ http://dx.doi.org/10.1039/C3CP54050B 


.. figure:: mol.png
    
    A=EthynPhA,R1=H,R2=H,R3=H
    
    
* `Download raw data <http://cmr.fysik.dtu.dk/dssc.db>`_
* `Browse data <http://casimir.fysik.dtu.dk:5000/?query=project%3Ddssc>`_


======  ====================================================
key     description
======  ====================================================
A       Anchor group
R1      First side group
R2      Second side group
R3      Third side group
HOMO    Kohn-Sharm HOMO eigenvalue
LUMO    Kohn-Sharm LUMO eigenvalue
ks_gap  Kohn-Sharm eigenvalue electronic gap (LUMO - HOMO)
IP      Ionization potential
EA      Electron affinity
de_gap  Electronic gap (IP - EA)
======  ====================================================


Example use of data
-------------------

.. include:: gaps.py
   :code: python

.. image:: gaps.svg
   :width: 600

