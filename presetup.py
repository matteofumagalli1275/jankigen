import zipfile
from os import path

dbpath = path.dirname(__file__) + "/jankigen/res/jamdict.zip"
dbpathdir = path.dirname(__file__) + "/jankigen/res/"
with zipfile.ZipFile(dbpath, 'r') as zip_ref:
    zip_ref.extractall(dbpathdir)