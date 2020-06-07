import setuptools
# read the contents of your README file
from os import path
from jankigen.version import version_string

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', 'r') as infile:
    requirements = infile.read().splitlines()
    print(requirements)

setuptools.setup(name='jankigen',
                 version=version_string,
                 packages=setuptools.find_packages(),
				 package_data={'jankigen': ['res/jamdict.db', 'res/favicon.ico']},
                 entry_points={
                     'console_scripts': [
                         'jankigen = jankigen.__main__:main'
                     ]
                 },
                 install_requires=requirements,
                 description="Generate Anki decks from Japanese text",
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 options={'py2exe': {'bundle_files': 1, 'compressed': True}},
                 )
