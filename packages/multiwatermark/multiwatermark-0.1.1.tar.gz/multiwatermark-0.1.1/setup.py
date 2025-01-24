from setuptools import setup, find_packages
setup(
name='multiwatermark',
version='0.1.1',
author='Matt Burns',
author_email='mburns7211@gmail.com',
description='Add custom watermarks to images',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
install_requires=['pillow'],
python_requires='>=3.8',
)
