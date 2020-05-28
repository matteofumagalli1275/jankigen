import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(name='jankigen',
                 version='0.1.1',
                 packages=setuptools.find_packages(),
                 entry_points={
                     'console_scripts': [
                         'jankigen = jankigen.__main__:main'
                     ]
                 },
                 install_requires=[
                     'genanki',
                     'jamdict',
                     'janome'
                 ],
                 description="Generate Anki decks from Japanese text",
                 long_description=long_description,
                 long_description_content_type='text/markdown'
                 )
