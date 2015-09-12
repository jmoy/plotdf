from setuptools import setup,find_packages

setup(
  name = "plotdf",
  version = "0.1",
  description = "Plot phase portraits of 2D differential equations",
  url = "https://github.com/jmoy/plotdf",
  
  author = "Jyotirmoy Bhattacharya",
  author_email = "jyotirmoy@jyotirmoy.net",
  license = "GPLv3",

  classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
  ],

  keywords = 'matplotlib differential-equations numerics plot',

  packages = find_packages(),

  install_requires = ["numpy","matplotlib","scipy"],
)
