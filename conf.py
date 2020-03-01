# -*- coding: utf-8 -*-

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from datetime import datetime

# General configuration
extensions = [
    'sphinx.ext.autosectionlabel',
    'recommonmark',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.rst']
templates_path = ['_templates']
numfig = True
numfig_format = {
    'figure': 'Figure %s', 
    'table': 'Table %s',
    'code-block': '例 %s', 
    'section': 'Section %s'
    }

# Internationalization
language = 'zh_CN'

# Porject information
project = 'Yang的笔记'
copyright = '2018-{}, YANG'.format(datetime.now().year)
author = 'yang'
version = '0.1.0'
release = version

# HTML output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
html_static_path = ['_static']
html_logo = '_static/logo.png'
html_favicon = '_static/favicon.ico'

# LaTeX output
latex_engine = 'xelatex'
latex_documents = [('index', 'yang.tex', 'Yang的笔记',
                    'Yang DONG', 'manual', 1)]
latex_logo = '_static/logo.png'
latex_show_urls = 'footnote'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}
