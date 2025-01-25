from setuptools import setup, find_packages

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
name='multiwatermark',
version='0.1.3',
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
long_description=long_description,
long_description_content_type='text/markdown'
)
