New Light Harvesting Materials
==============================

.. container:: article

    Ivano E. Castelli, Falco Hüser, Mohnish Pandey, Hong Li,
    Kristian S. Thygesen, Brian Seger, Anubhav Jain, Kristin Persson,
    Gerbrand Ceder, and Karsten W. Jacobsen

    `New Light Harvesting Materials Using Accurate and Efficient Bandgap
    Calculations`__

    Advanced Energy Materials, Juli 22, 2014

    __ http:/dx.doi.org/10.1002/aenm.201400915

* :download:`Download raw data <mp_gllbsc.db>`
* `Browse data <http://cmrdb.fysik.dtu.dk/?query=project%3Dmp_gllbsc>`_


Key-value pairs
---------------

==============  =============================================================
key             description
==============  =============================================================
gllbsc_dir_gap  Direct bandgap calculated with GLLB-SC.
gllbsc_ind_gap  Indirect bandgap calculated with GLLB-SC.
gllbsc_disc     Derivative discontinuity calculated with GLLB-SC.
mpid            "Materials project" id
g0w0_gap        `G_0W_0` gap at `\Gamma`
gw0_gap         `GW_0` gap at `\Gamma`
gw_gap          `GW` gap at `\Gamma`
hse06_gap       HSE06 gap at `\Gamma`
lda_gap         LDA gap at `\Gamma`
gllbsc_gap      GLLBSC gap at `\Gamma`
project         Name of the project: "mp_gllbsc"
==============  =============================================================


Band gaps
---------

Here, we calculated the errors in the band gaps at `\Gamma` for a set of 20
ternary and quaternary materials releative to self-consitent GW:

.. literalinclude:: table.py
    :start-after: future
    
.. csv-table::
    :file: gaps.csv
    :header-rows: 1
    
.. image:: gaps.svg

Here is how to make the plot:

.. literalinclude:: figure.py
