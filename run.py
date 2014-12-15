from __future__ import print_function
import os
import urllib
from ase.utils.sphinx import create_png_files

url = 'https://cmr.fysik.dtu.dk/_downloads/'
projects = [('dssc', ['dssc']),
            ('beef', ['beef', 'beefgpaw']),
            ('mp_gllbsc', ['mp_gllbsc']),
            ('organometal', ['organometal']),
            ('cubic_perovskites', ['cubic_perovskites']),
            ('low_symmetry_perovskites', ['low_symmetry_perovskites'])]

for name, dbs in projects:
    for db in dbs:
        path = os.path.join(name, db + '.db')
        if not os.path.isfile(path):
            print('Dowloading', path)
            urllib.urlretrieve(url + db + '.db', path)
        
create_png_files(run_all_python_files=True, exclude=['./run.py', './conf.py'])
