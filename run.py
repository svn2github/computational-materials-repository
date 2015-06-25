from __future__ import print_function
import os
import shutil
import urllib

from ase.utils.sphinx import create_png_files, clean


url = 'https://cmr.fysik.dtu.dk/_downloads/'
downloads = [('dssc', ['dssc.db']),
             ('dcdft', ['dcdft.db', 'dcdft_gpaw_pw_paw09.db']),
             ('beef', ['molecules.db', 'solids.db']),
             ('mp_gllbsc', ['mp_gllbsc.db']),
             ('organometal', ['organometal.db']),
             ('cubic_perovskites', ['cubic_perovskites.db']),
             ('low_symmetry_perovskites', ['low_symmetry_perovskites.db']),
             ('c2dm', ['c2dm.db']),
             ('vdwh', ['chi-data.tar.gz']),
             ('tmfp06d', ['tmfp06d.db']),
             ('absorption_perovskites', ['absorption_perovskites.db']),
             ('funct_perovskites', ['funct_perovskites.db']),
             ('fcc111', ['fcc111.db']),
             ('compression', ['compression.db'])]

# Add pictures for the front-page:
downloads += [('.', [dir + '.png' for dir, names in downloads])]


def download():
    """Download the big data files and front-page images for each project."""
    for dir, names in downloads:
        for name in names:
            path = os.path.join(dir, name)
            if not os.path.isfile(path):
                print('Downloading', path)
                if dir == '.':
                    name = '../_images/' + name
                urllib.urlretrieve(url + name, path)

                
def setup(app):
    """Sphinx entry point."""
    download()
    create_png_files()


if __name__ == '__main__':
    # Run this on the web-server only:
    clean()
    for dir, names in downloads:
        for name in names:
            path = os.path.join(dir, name)
            if not os.path.isfile(path):
                print('Copying', path)
                shutil.copy(os.path.join('..', 'downloads', name), path)
