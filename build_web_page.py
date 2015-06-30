"""Script for server that builds the CMR web-page continuously."""
from __future__ import print_function
import optparse
import os
import shutil
import subprocess
import sys

from ase.utils.build_web_page import svn_update
from ase.utils.sphinx import clean
from downloads import downloads

        
def build():
    home = os.getcwd()
    os.chdir('cmr')
    # Run this on the web-server only:
    shutil.rmtree('build')
    clean()  # remove all generated files (.png, .svg, .csv, ...)
    for dir, names in downloads:
        for name in names:
            path = os.path.join(dir, name)
            if not os.path.isfile(path):
                print('Copying', path)
                shutil.copy(os.path.join('..', 'downloads', name), path)
    os.makedirs('build/html')  # Sphinx-1.1.3 needs this (1.2.2 is OK)
    subprocess.check_call('PYTHONPATH={0}/ase make html'.format(home),
                          shell=True)
           
    # Use https for mathjax:
    subprocess.check_call(
        'find build -name "*.html" | '
        'xargs sed -i "s|http://cdn.mathjax.org|https://cdn.mathjax.org|"',
        shell=True)

    os.chdir('build')
    os.rename('html', 'cmr-web-page')
    subprocess.check_call('tar -czf cmr-web-page.tar.gz cmr-web-page',
                          shell=True)
    os.rename('cmr-web-page.tar.gz', '../../cmr-web-page.tar.gz')
    os.chdir('../..')


def main():
    """Build web-page if there are changes in the source."""
    if os.path.isfile('build-web-page.lock'):
        print('Locked', file=sys.stderr)
        return
    try:
        with open('build-web-page.lock', 'w'):
            pass
            
        parser = optparse.OptionParser(usage='Usage: %prog [-f]',
                                       description='Build web-page')
        parser.add_option('-f', '--force-build', action='store_true',
                          help='Force build instead of building only when '
                          'there are changes to the docs or code.')
        opts, args = parser.parse_args()
        assert len(args) == 0
        changes = svn_update('ase')
        changes |= svn_update('cmr')
        if opts.force_build or changes:
            build()
    finally:
        print(os.getcwd())
        os.remove('build-web-page.lock')

        
if __name__ == '__main__':
    main()
