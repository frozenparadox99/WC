from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 1 - Planning',
  'Intended Audience :: Education',
  'Operating System :: MacOS :: MacOS X',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='wcom',
  version='0.0.1',
  description='A simple library for solving WC questions',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/frozenparadox99/WC',
  author='Pratyush Kerhalkar',
  author_email='pratyushkerhalkar@gmail.com',
  license='MIT',
  classifiers=classifiers,
  keywords='wireless communication',
  packages=find_packages(),
  install_requires=['']
)
