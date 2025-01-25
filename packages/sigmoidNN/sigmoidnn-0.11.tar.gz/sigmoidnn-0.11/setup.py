from setuptools import setup, find_packages

setup(
  name='sigmoidNN',
  version='0.11',
  packages=find_packages(),
  install_requires=[
    'numpy'
  ],
  author='anas',
  author_email='anas.ahamad955@gmail.com',
  description='sigmoid neural network library',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/Anas-github-Acc/SigmoidNN-package',
  include_package_data=True,
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
)