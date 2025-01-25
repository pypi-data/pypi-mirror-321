from distutils.core import setup
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
  name = '102217053_topsis',
  packages = ['102217053_topsis'],
  version = '1.0.3',
  license='MIT',
  long_description=long_description,
  long_description_content_type="text/markdown",  # Important for Markdown
  description = 'This is a topsis package',
  author = 'Mitul Agarwal',
  author_email = 'mitulagarwal2003@gmail.com',
  url = 'https://github.com/user/reponame',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['topsis'],
  install_requires=[
          'pandas',
          'numpy',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)