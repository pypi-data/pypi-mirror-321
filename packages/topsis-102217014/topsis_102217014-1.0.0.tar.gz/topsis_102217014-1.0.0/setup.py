from setuptools import setup, find_packages

setup(
  name = 'topsis-102217014',                 
  packages = find_packages(),                  
  version = '1.0.0',                                
  description = 'Topsis',
  author = 'Aaditya', 
  author_email = 'thakuraaditya1024@gmail.com',
  install_requires = ['numpy', 'pandas'],
  scripts=['main.py']
)