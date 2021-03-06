import sys
sys.path[:0] = ['.']
extensions = ['run_python_scripts',
              'sphinx.ext.intersphinx',
              'sphinx.ext.mathjax']
source_suffix = '.rst'
master_doc = 'index'
project = u'COMPUTATIONAL MATERIALS REPOSITORY'
copyright = u'2014, CAMd'
exclude_patterns = ['build']
pygments_style = 'sphinx'
default_role = 'math'
html_theme = 'haiku'
html_style = 'cmr.css'
html_title = 'COMPUTATIONAL MATERIALS REPOSITORY'
html_favicon = 'static/cmr.ico'
html_static_path = ['static']
html_last_updated_fmt = '%a, %d %b %Y %H:%M:%S'
intersphinx_mapping = {'ase': ('http://wiki.fysik.dtu.dk/ase', None)}
