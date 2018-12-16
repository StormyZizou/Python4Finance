#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil
from shutil import make_archive

parent_folder = r"C:\Users\bharakumar\Desktop"

def pack_it(source_folder):
    #Zips the folder contents to the parent fodler
    shutil.make_archive(os.path.join(parent_folder, os.path.basename(source_folder)), 'zip', source_folder)

def pack_it_to(source_folder, destination_folder):
    #Zips the contents of a folder to another folder
    shutil.make_archive(os.path.join(destination_folder, os.path.basename(source_folder)), 'zip', source_folder)

def pack_all(parent_folder, folders_to_pack=None):
    #Zips each of the listed folders in folders_to_pack and saves the zip file in the same directory
    if folders_to_pack == None:
        folders_to_pack = [dI for dI in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder,dI))]
        print("folders to pack are %s" %folders_to_pack)
    for folder_name in folders_to_pack:
        shutil.make_archive(os.path.join(parent_folder, folder_name), 'zip', os.path.join(parent_folder, folder_name))
        
def pack_all_to(parent_folder, destination_folder, folders_to_pack = None):
    #Zips each of the listed folders in folders_to_pack and saves the zip file in the same directory
    if folders_to_pack == None:
        folders_to_pack = [dI for dI in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder,dI))]
        print("folders to pack are %s" %folders_to_pack)
    for folder_name in folders_to_pack:
        shutil.make_archive(os.path.join(destination_folder, folder_name), 'zip', os.path.join(parent_folder, folder_name))

