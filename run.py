from __future__ import print_function
import optparse
import os
import shutil
import urllib

from ase.utils.sphinx import create_png_files

url = 'https://cmr.fysik.dtu.dk/_downloads/'
downloads = [('dssc', ['dssc.db']),
             ('dcdft', ['dcdft.db', 'dcdft_gpaw_pw_paw09.db']),
             ('beef', ['beef.db', 'beefgpaw.db']),
             ('mp_gllbsc', ['mp_gllbsc.db']),
             ('organometal', ['organometal.db']),
             ('cubic_perovskites', ['cubic_perovskites.db']),
             ('low_symmetry_perovskites', ['low_symmetry_perovskites.db']),
             ('c2dm', ['c2dm.db', 'chi-data.tar.gz']),
             ('tmfp06d', ['tmfp06d.db'])]
downloads += [('.', [dir + '.png' for dir, names in downloads])]

parser = optparse.OptionParser()
parser.add_option('--copy', action='store_true')
opts, args = parser.parse_args()
if args:
    parser.error('sdfg')
    
for dir, names in downloads:
    for name in names:
        path = os.path.join(dir, name)
        if not os.path.isfile(path):
            if opts.copy:
                print('Copying', path)
                shutil.copy(os.path.join('..', 'downloads', name), path)
            else:
                print('Downloading', path)
                if dir == '.':
                    name = '../_images/' + name
                urllib.urlretrieve(url + name, path)
        
create_png_files()
