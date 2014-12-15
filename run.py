from __future__ import print_function
import os
import shutil
import sys
import urllib
from ase.utils.sphinx import create_png_files

copy = False
if len(sys.argv) == 2 and sys.argv[1] == 'copy':
    copy = True

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
            if copy:
                print('Copying', path)
                shutil.copy(os.path.join('..', 'db-files', db + '.db'), path)
            else:
                print('Dowloading', path)
                urllib.urlretrieve(url + db + '.db', path)
        
create_png_files(run_all_python_files=True, exclude=['./run.py', './conf.py'])
