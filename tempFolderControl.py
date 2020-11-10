#Temp Folder Control by Fábio Pinto
from os import makedirs
from shutil import rmtree
path = "d:\\#TEMP"
try:
    rmtree(path)
except:
    print('Directory not found')
finally:
    makedirs(path)
