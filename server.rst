.. _server:
.. highlight:: bash

=======================
Setting up a web-server
=======================

The CMR web-pages
=================

To get started from scratch::
    
  $ cd ~
  $ mkdir sphinx
  $ cd sphinx
  $ svn co https://svn.fysik.dtu.dk/projects/cmr2/trunk cmr
  $ svn co https://svn.fysik.dtu.dk/projects/ase/trunk ase
  $ mkdir downloads
  
Put db-files and images for the front-page in the *download* folder. Then run
:download:`build_web_page.py` from your crontab::
    
  MAILTO=...
  PP=$HOME/sphinx/ase:$PYTHONPATH
  */15 * * * * cd ~/sphinx && PYTHONPATH=$PP python cmr/build_web_page.py > cmr.log


The CMR database
================

See https://intra4.fysik.dtu.dk/it/Niflheim_cmrdb-6.
