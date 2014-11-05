from __future__ import print_function
import os
import urllib
from ase.utils.sphinx import create_png_files

url = 'https://cmr.fysik.dtu.dk/_downloads/'
projects = ['dssc',
            'mp_gllbsc',
            'organometal',
            'cubic_perovskites',
            'low_symmetry_perovskites']

for name in projects:
    path = os.path.join(name, name + '.db')
    if not os.path.isfile(path):
        print('Dowloading', path)
        urllib.urlretrieve(url + name + '.db', path)
        
create_png_files(run_all_python_files=True, exclude=['./run.py', './conf.py'])
