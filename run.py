from __future__ import print_function
import optparse
import os
import shutil
import urllib

import ase.db
from ase.utils.sphinx import create_png_files

url = 'https://cmr.fysik.dtu.dk/_downloads/'
projects = [('dssc', ['dssc.db']),
            ('dcdft', ['dcdft.db', 'dcdft_gpaw_pw_setups09.db']),
            ('beef', ['beef.db', 'beefgpaw.db']),
            ('mp_gllbsc', ['mp_gllbsc.db']),
            ('organometal', ['organometal.db']),
            ('cubic_perovskites', ['cubic_perovskites.db']),
            ('low_symmetry_perovskites', ['low_symmetry_perovskites.db']),
            ('c2dm', ['c2dm.db', 'chi-data.tar.gz'])]

parser = optparse.OptionParser()
parser.add_option('--copy', action='store_true')
parser.add_option('--build-db')
opts, args = parser.parse_args()
if args:
    parser.error('sdfg')
    
for name, dbs in projects:
    for db in dbs:
        path = os.path.join(name, db)
        if not os.path.isfile(path):
            if opts.copy:
                print('Copying', path)
                shutil.copy(os.path.join('..', 'db-files', db), path)
            else:
                print('Dowloading', path)
                urllib.urlretrieve(url + db, path)
        
create_png_files()

if opts.build_db:
    for name, dbs in projects:
        for db in dbs:
            if not db.endswith('db'):
                continue
            path = os.path.join(name, db)
            with ase.db.connect(opts.build_db) as big:
                for d in ase.db.connect(path).select():
                    big.write(d,
                              data=d.get('data'),
                              **d.get('key_value_pairs', {}))
