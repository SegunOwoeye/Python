#Python 3.6

import os
import shutil

os.system("clear")
def d():

    Filing_Parameter= input("Input File Name: ")
    Filing_Parameter = str(Filing_Parameter)
    os.system("clear")

    victim_path = "/Users/SegunOwoeye/Desktop/"
    usb_path = "/Volumes/USB/Copied Files/Desktop/"
    names = os.listdir(victim_path)

    dirs = [x[0] for x in os.walk("/Users/SegunOwoeye/Desktop/")]

    #Checks Surface of Directory in the Desktop

    for files in names:
        if Filing_Parameter in files and not os.path.exists(usb_path+files):
            shutil.copytree(victim_path+files, usb_path +files+"/")

    #Walks through all Subdirectories in the Desktop Folder
    for files in dirs:
        if Filing_Parameter in files and not os.path.exists(usb_path+files):
            shutil.copytree(files, usb_path+files)


d()
            
print("File Transfer Complete")