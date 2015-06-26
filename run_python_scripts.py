from __future__ import print_function
import os
import urllib
from ase.utils.sphinx import create_png_files
from downloads import downloads

url = 'https://cmr.fysik.dtu.dk/_downloads/'


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
