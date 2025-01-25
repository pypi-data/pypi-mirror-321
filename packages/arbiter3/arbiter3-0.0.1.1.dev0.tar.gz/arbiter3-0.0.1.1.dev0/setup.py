#!/usr/bin/env python

from distutils.core import setup

setup(name='arbiter3',
      version='0.0.1',
      description='Python Distribution Utilities',
      author='Kai Forrest, Jackson McKay',
      author_email='kai.forrest@utah.edu, jay.mckay@utah.edu',
      url='https://github.com/CHPC-UofU/arbiter',
      packages=['arbiter3'],
      entry_points={
          'console_scripts': ['arbiter3 = arbiter3.manage:main']
      }
     )