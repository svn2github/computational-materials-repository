.. _dcdft:

DeltaCodesDFT
=============

Codes precision measured using the
database of bulk systems from http://molmod.ugent.be/DeltaCodesDFT.
See the project page for details.

* :download:`Download raw data for all codes <dcdft.db>`
* :download:`Download raw GPAW data for PAW datasets version 0.9 <dcdft_gpaw_pw_setups09.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Ddcdft&
  toggle=user,calculator,name,x,xc,kptdensity,width,energy,volume>`_

.. contents::
    
Key-value pairs
---------------

===========  =============================================================
key          description
===========  =============================================================
kptdensity   K-point density in point per Ang^-1
linspacestr  Numpy's linspace used for scaling the cell along the EOS
name         Name of the elemental bulk system (H-Ba, Lu-Po, Rn)
project      Name of the project: "dcdft"
width        Electronic temperature
x            Strain used to scale the cell along the EOS (see linspacestr)
===========  =============================================================

Note that there are additional keys not explained above which are
specific to the given calculator.


GPAW results for PAW datasets version 0.9
-----------------------------------------

Running the following script writes the EOS parameters: V0 in Å**3/atom,
bulk modulus (B0) in GPa,
and pressure derivative of the bulk modulus B1 (dimensionless), in a file
format expected by the calcDelta.py script available from http://molmod.ugent.be/DeltaCodesDFT

.. literalinclude:: extract.py
    :start-after: future


Results from other codes
------------------------

Consists of two steps. First extract the data for the given code and
insert it into a new database file. Then use the extract.py script
above to write the formatted file using the data from the new database file.

.. literalinclude:: extract.sh

A typical example of analysing data could be a verification
of the results stored http://molmod.ugent.be/DeltaCodesDFT against
the database.

.. literalinclude:: aims_tight.sh


Running the calculations again
------------------------------

Selected scripts used to obtain the results are available at
https://wiki.fysik.dtu.dk/gpaw/setups/dcdft.html
