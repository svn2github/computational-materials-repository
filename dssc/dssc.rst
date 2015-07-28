.. _dssc:

Porphyrin based dyes
===================================
The first 5145 porphyrins are described in:

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
   
Examples of using the database can be found in:

.. container:: article
  
    Kristian B. Ørnsø, Juan M. García-Lastra, Gema De La Torre,
    F. J. Himpsel, Angel Rubio and Kristian S. Thygesen

    `Design of two-photon molecular tandem architectures for solar
    cells by ab initio theory <http://dx.doi.org/10.1039/C4SC03835E>`_

    Chem. Sci., 2015, 6, 3018-3025

.. container:: article
  
    Kristian B. Ørnsø, Elvar Ö. Jónsson, Karsten W. Jacobsen and
    Kristian S. Thygesen

    `Importance of the Reorganization Energy Barrier in Computational
    Design of Porphyrin-Based Solar Cells with Cobalt-Based Redox
    Mediators <http://dx.doi.org/10.1021/JP512627E>`_

    J. Phys. Chem. C, 2015, 119, 12792-12800

.. contents::
        
* :download:`Download raw data <dssc.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Ddssc&
  toggle=user,pbc,volume,E_gap,KS_gap>`_


Key-value pairs
---------------

.. figure:: mol.png
    
   Example of dye with: M=ZnP, A=EthynPhA, R1=Ph, R2=Ph, R3=Ph

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
   :code: python

.. image:: homolumo.svg
   :width: 600

List of structure related keywords
----------------------------------

+---------------+---------------------+---------------------------+
|Metal centers  | Side groups         |  Anchor groups            |
+===============+=====================+===========================+
| ZnP           | Ph                  | EthynPhA                  |
+---------------+---------------------+---------------------------+
| FZnP          | FPh                 | 2CyanoPropenA             |
+---------------+---------------------+---------------------------+
| H2P           | DMP                 | 2CarboxyPropenA           |
+---------------+---------------------+---------------------------+
| FH2P          | TPA                 | EthenThPCyanoAcryl        |
+---------------+---------------------+---------------------------+
| TiOP          | MOTPA               | EthynBTDPhA               |
+---------------+---------------------+---------------------------+
| FTiOP         | TMP                 | EthynDPhEPhA              |
+---------------+---------------------+---------------------------+
| TiO2RP        | DTA                 | EthynPhEPhA               |
+---------------+---------------------+---------------------------+
| FTiO2RP       | DTBP                | EthynTPhEPhA              |
+---------------+---------------------+---------------------------+
|               | EthynPhM (only R2)  | EthynPhDA                 |
+---------------+---------------------+---------------------------+
|               |                     | EthynFuA                  |
+---------------+---------------------+---------------------------+
|               |                     | EthynThPCyanoAcryl        |
+---------------+---------------------+---------------------------+
|               |                     | EthynDThPCyanoAcryl       |
+---------------+---------------------+---------------------------+
|               |                     | DThPCyanoAcryl            |
+---------------+---------------------+---------------------------+
|               |                     | ThPCyanoAcryl             |
+---------------+---------------------+---------------------------+
|               |                     | EthynThPA                 |
+---------------+---------------------+---------------------------+
|               |                     | EthynDThPA                |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynPhA              |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthenThPCyanoAcryl    |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynBTDPhA           |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynDPhEPhA          |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynPhEPhA           |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynTPhEPhA          |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynPhDA             |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynFuA              |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynThPCyanoAcryl    |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynDThPCyanoAcryl   |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynThPA             |
+---------------+---------------------+---------------------------+
|               |                     | rot-EthynDThPA            |
+---------------+---------------------+---------------------------+
