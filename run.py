from __future__ import print_function
import optparse
import os
import shutil
import urllib

import ase.db
from ase.utils.sphinx import create_png_files

url = 'https://cmr.fysik.dtu.dk/_downloads/'
projects = [('dssc', ['dssc']),
            ('dcdft', ['dcdft', 'dcdft_gpaw_pw_setups09']),
            ('beef', ['beef', 'beefgpaw']),
            ('mp_gllbsc', ['mp_gllbsc']),
            ('organometal', ['organometal']),
            ('cubic_perovskites', ['cubic_perovskites']),
            ('low_symmetry_perovskites', ['low_symmetry_perovskites']),
            ('c2dm', ['c2dm'])]

parser = optparse.OptionParser()
parser.add_option('--copy', action='store_true')
parser.add_option('--build-db')
opts, args = parser.parse_args()
if args:
    parser.error('sdfg')
    
for name, dbs in projects:
    for db in dbs:
        path = os.path.join(name, db + '.db')
        if not os.path.isfile(path):
            if opts.copy:
                print('Copying', path)
                shutil.copy(os.path.join('..', 'db-files', db + '.db'), path)
            else:
                print('Dowloading', path)
                urllib.urlretrieve(url + db + '.db', path)
        
create_png_files()

if opts.build_db:
    for name, dbs in projects:
        for db in dbs:
            path = os.path.join(name, db + '.db')
            with ase.db.connect(opts.build_db) as big:
                for d in ase.db.connect(path).select():
                    big.write(d,
                              data=d.get('data'),
                              **d.get('key_value_pairs', {}))
