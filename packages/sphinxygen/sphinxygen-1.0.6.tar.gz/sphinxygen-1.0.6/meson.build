# Copyright 2021-2025 David Robillard <d@drobilla.net>
# SPDX-License-Identifier: 0BSD OR ISC

project(
  'sphinxygen',
  [],
  license: 'ISC',
  meson_version: '>= 0.56.0',
  version: '1.0.6',
)

pymod = import('python')

py = pymod.find_installation(
  'python3',
  modules: [
    'argparse',
    'textwrap',
    'xml.etree.ElementTree',
  ],
)

init_py = files('src/sphinxygen/__init__.py')
sphinxygen_py = files('src/sphinxygen/sphinxygen.py')

# Override program for internal meson dependants
meson.override_find_program('sphinxygen', sphinxygen_py)

# Install executable script
sphinxygen = executable(
  'sphinxygen',
  sphinxygen_py,
  install_dir: get_option('bindir')
)

summary(
  {
    'Install prefix':  get_option('prefix'),
    'Executables': get_option('prefix') / get_option('bindir'),
  },
  section: 'Directories',
)
