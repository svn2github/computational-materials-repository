What is CMR?
============

...


Working with the databases
--------------------------

* :ref:`ase-db <ase:ase-db>` command-line tool
* :mod:`ase.db` Python module
* :ref:`web-interface <ase:ase-db-web>`


Building this web-page
----------------------

Check out the source::
    
    $ svn co https://svn.fysik.dtu.dk/projects/cmr2/trunk cmr
    $ cd cmr
    
Make sure you have an up to date :ref:`ASE <ase:download_and_install>` and
Sphinx_ installation.  Then do::
    
    $ python run.py
    
This will download the database files and run Python scripts to create images
and other stuff needed for the webpages (.svg and .csv files).

Build the html-files::
    
    $ make

.. _Sphinx: http://sphinx.pocoo.org/


Modifying the pages
-------------------

Edit the ReST and Python files (.rst and .py files) and then run ``make``
again and check the results::
    
    $ make
    $ firefox build/html/index.html

When things are OK, you can ``svn commit`` the updated files and the
*cmr.fysik.dtu.dk* webpage will be updated automatically within an hour.
