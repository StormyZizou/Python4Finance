# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:17:48 2018

@author: pa89000
"""

import os
import zipfile
import shutil

source_folder = r"C:\Users\pa89000\Desktop\lol_p\lol"
destination_folder = r"C:\Users\pa89000\Desktop\lol_d"
src = r"C:\Users\pa89000\Desktop\lol_p\compress.zip" #zipfile in source folder

def main():
    
    pack_it(source_folder)
    pack_it_to(src, destination_folder)
    
def pack_it(source_folder):
"""
Add description comments to functions. This enables using the __help__ in Python

"""
    zipf = r"C:\Users\pa89000\Desktop\lol_p\compress.zip" # GA:  this should be an input for the function to be used anywhere
    zippedHelp = zipfile.ZipFile(zipf, "w", compression=zipfile.ZIP_DEFLATED )
    list = os.listdir(source_folder)
    for file_list in list:                                # GA: "list" is not a good choice of name for a variable
        file_name = os.path.join(source_folder,file_list)

        if os.path.isfile(file_name):
            print file_name
            zippedHelp.write(file_name)
        else:
            addFolderToZip(zippedHelp,file_list,source_folder)
            print "Folder Found"
    zippedHelp.close() 

def addFolderToZip(zippedHelp,folder,source_folder):
"""
Good logic to use a "Recursive function" to navigate through sub-folders. An alternate optimal way could have been to get the file_paths of all constituents using the library os and then zip all those paths.

Also, look at the folder structure with in the zip file that is created. It retains all the sub-folders, which would be sub-optimal in the case we are zipping a deeply nested folder. 

"""
    path=os.path.join(source_folder,folder)
    print path
    file_list=os.listdir(path)
    for file_name in file_list:
        file_path=os.path.join(path,file_name)
        if os.path.isfile(file_path):
            zippedHelp.write(file_path)
        elif os.path.isdir(file_name):
            print "sub folder found"
            addFolderToZip(zippedHelp,file_name,path)
            
def pack_it_to(src, destination_folder):
    shutil.copy(src,destination_folder)
    print"Zipfile moved to Destination folder"
    
if __name__=="__main__":
    main()

    

    
