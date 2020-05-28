import setuptools

setuptools.setup(name='jankigen',
                 version='0.1.0',
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
                 )
