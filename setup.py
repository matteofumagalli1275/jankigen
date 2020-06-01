import setuptools
# read the contents of your README file
from os import path
from jankigen.version import version_string

import zipfile
dbpath = path.dirname(__file__) + "jankigen/db/jamdict.zip"
dbpathdir = path.dirname(__file__) + "jankigen/db/"
with zipfile.ZipFile(dbpath, 'r') as zip_ref:
    zip_ref.extractall(dbpathdir)


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='jankigen',
                 version=version_string,
                 packages=setuptools.find_packages(),
				 package_data={'jankigen': ['db/jamdict.db', 'favicon.ico']},
                 entry_points={
                     'console_scripts': [
                         'jankigen = jankigen.__main__:main'
                     ]
                 },
                 install_requires=[
                     'genanki',
                     'jamdict',
                     'janome',
                     'ttkthemes'
                 ],
                 description="Generate Anki decks from Japanese text",
                 long_description=long_description,
                 long_description_content_type='text/markdown',
                 options={'py2exe': {'bundle_files': 1, 'compressed': True}},
                 )
