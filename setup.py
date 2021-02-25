import sys
from setuptools import setup, find_packages

version = sys.version_info
if version == (3, 7):
    sys.stderr.write('requires Python 3.7\n')
    sys.exit(1)

PACKAGE_NAME = "url_shortening"
PACKAGE_VERSION = "1.0"

SUMMARY = "Web Service to create short URLs"

DESCRIPTION = "Web Service allows to create short URLSs and get original URL from short URL"

dependencies = ['flask', 'flask_sqlalchemy', 'requests']

setup(name=PACKAGE_NAME,
      version=PACKAGE_VERSION,
      author="EvgT",
      description=SUMMARY,
      long_description=DESCRIPTION,
      packages=find_packages(),
      install_requires=dependencies)
