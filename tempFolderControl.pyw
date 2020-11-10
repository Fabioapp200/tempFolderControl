#Temp Folder Control by Fábio Pinto
import os
from shutil import rmtree
from win10toast import ToastNotifier
toaster = ToastNotifier()
path = "D:\#TEMP"
try:
    rmtree(path)
    os.makedirs(path)
except:
    print('Erro')
toaster.show_toast('Temp Folder Control', '#TEMP Folder Cleared')