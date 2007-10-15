from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='elementtreewriter',
      version=version,
      description="XML writer for elementrees with sane namespace support.",
      long_description="""\
TODO""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='xml elementtree',
      author='Martin Raspe, Jens Klein',
      author_email='hertzhaft@biblhertz.it, jens@bluedynamics.com',
      url='',
      license='D-FSL - German Free Software License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
      
