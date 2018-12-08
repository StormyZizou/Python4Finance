#!/usr/bin/env python
# coding: utf-8

# In[409]:


#Importing libraries
import os
import shutil

os.system('cls')


# In[394]:


#Packs all the folders in the source folder
def pack_it(source_folder):
    Full_dir_list=os.listdir() #List of files and directories/folders in the source folder
    len_total_dir=len(Full_dir_list) #Number of files and directories in the source folder
    zip_folder_path=[]
    suffix='.zip'
    for i in range(len_total_dir):
        zip_folder_path=os.path.join(source_folder,Full_dir_list[i]) #Path for each file or folder in the source folder
        if os.path.isdir(zip_folder_path): #Packs only folders and not files
            if os.path.isfile(os.path.join(source_folder,Full_dir_list[i]+suffix)): #Check if the zip file already exists in the source folder
                File_Name= Full_dir_list[i]+suffix
                print(File_Name,'already exists')
            else:
                shutil.make_archive(Full_dir_list[i],'zip', zip_folder_path) #Creates the zip file


# In[395]:


#Packs all the folders in the source folder and move them to destination folder
def pack_it_to(source_folder,destination_folder):
    Full_dir_list=os.listdir() #List of files and directories/folders in the source folder
    len_total_dir=len(Full_dir_list) #Number of files and directories in the source folder
    zip_folder_path=[]
    suffix='.zip'
    for i in range(len_total_dir):
        zip_folder_path=os.path.join(source_folder,Full_dir_list[i]) #Path for each file or folder in the source folder
        if os.path.isdir(zip_folder_path): #Packs only folders and not files
            if os.path.isfile(os.path.join(destination_folder,Full_dir_list[i]+suffix)): #Check if the zip file already exists in the destination folder
                File_Name= Full_dir_list[i]+suffix
                print(File_Name,'already exists')
                if os.path.isfile(os.path.join(source_folder,Full_dir_list[i]+suffix)): #Check if the zip file already exists in the source folder and delete it
                    os.remove(os.path.join(source_folder,Full_dir_list[i]+suffix))
            else:
                shutil.make_archive(Full_dir_list[i],'zip', zip_folder_path) #Creates the zip file
                shutil.move(zip_folder_path+suffix,destination_folder) #Move the zip file to destination folder


# In[400]:


#Packs all the folders in the source folder or the specific folders
def pack_all(source_folder,folders_to_pack=None):
    zip_folder_path=[]
    suffix='.zip'
    if (folders_to_pack==None):
        Full_dir_list=os.listdir() #List of all files and directories/folders in the source folder
        len_total_dir=len(Full_dir_list) #Number of files and directories in the source folder
        for i in range(len_total_dir):
            zip_folder_path=os.path.join(source_folder,Full_dir_list[i]) #Path for each file or folder in the source folder
            if os.path.isdir(zip_folder_path): #Packs only folders and not files
                if os.path.isfile(os.path.join(source_folder,Full_dir_list[i]+suffix)): #Check if the zip file already exists in the source folder
                    File_Name= Full_dir_list[i]+suffix
                    print(File_Name,'already exists')
                else:
                    shutil.make_archive(Full_dir_list[i],'zip', zip_folder_path)  #Creates the zip file
    else:
        len_to_pack=len(folders_to_pack) #Number of directories or files inputted through folders_to_pack variable
        for i in range(len_to_pack):
            zip_folder_path=os.path.join(source_folder,folders_to_pack[i]) #Path for each file or folder in folders_to_pack list
            if os.path.isdir(zip_folder_path): #Packs only folders and not files
                if os.path.isfile(os.path.join(source_folder,folders_to_pack[i]+suffix)): #Check if the zip file already exists in the source folder
                    File_Name= folders_to_pack[i]+suffix
                    print(File_Name,'already exists')
                else:
                    shutil.make_archive(folders_to_pack[i],'zip', zip_folder_path) #Creates the zip file


# In[397]:


#Packs all the folders in the source folder or the specific folders and move them to destination folder
def pack_all_to(source_folder,destination_folder,folders_to_pack=None):
    zip_folder_path=[]
    suffix='.zip'
    if (folders_to_pack==None):
        Full_dir_list=os.listdir() #List of all files and directories/folders in the source folder
        len_total_dir=len(Full_dir_list) #Number of files and directories in the source folder
        for i in range(len_total_dir):
            zip_folder_path=os.path.join(source_folder,Full_dir_list[i]) #Path for each file or folder in the source folder
            if os.path.isdir(zip_folder_path): #Packs only folders and not files
                if os.path.isfile(os.path.join(destination_folder,Full_dir_list[i]+suffix)): #Check if the zip file already exists in the destination folder
                    File_Name= Full_dir_list[i]+suffix
                    print(File_Name,'already exists')
                    if os.path.isfile(os.path.join(source_folder,Full_dir_list[i]+suffix)): #Check if the zip file already exists in the source folder and delete it
                        os.remove(os.path.join(source_folder,Full_dir_list[i]+suffix))
                else:
                    shutil.make_archive(Full_dir_list[i],'zip', zip_folder_path) #Creates the zip file
                    shutil.move(zip_folder_path+suffix,destination_folder) #Move the zip file to destination folder
    else:
        len_to_pack=len(folders_to_pack) #Number of directories or files inputted through folders_to_pack variable
        for i in range(len_to_pack):
            zip_folder_path=os.path.join(source_folder,folders_to_pack[i])#Path for each file or folder in folders_to_pack list
            if os.path.isdir(zip_folder_path): #Packs only folders and not files
                if os.path.isfile(os.path.join(destination_folder,folders_to_pack[i]+suffix)): #Check if the zip file already exists in the destination folder
                    File_Name= folders_to_pack[i]+suffix
                    print(File_Name,'already exists')
                    if os.path.isfile(os.path.join(source_folder,folders_to_pack[i]+suffix)): #Check if the zip file already exists in the source folder and delete it
                        os.remove(os.path.join(source_folder,folders_to_pack[i]+suffix))
                else:
                    shutil.make_archive(folders_to_pack[i],'zip', zip_folder_path) #Creates the zip file
                    shutil.move(zip_folder_path+suffix,destination_folder) #Move the zip file to destination folder


# In[410]:


#Checking if the current working directory is same as the desired directory
Desired_directory= r'C:\Users\ndandu\Desktop\citi\Non FRTB Pricing Model\TestFX'

if os.getcwd()!=Desired_directory:
     os.chdir(Desired_directory)

#Setting the source folder to desired working directory        
source_folder= os.getcwd()

#Defining the destination folder
destination_folder=r'C:\Users\ndandu\Desktop\citi\Non FRTB Pricing Model\TestFx2'

folders_to_pack=['156363']


# In[ ]:


pack_it(source_folder)
pack_it_to(source_folder,destination_folder)
pack_all(source_folder)
pack_all(source_folder,folders_to_pack=folders_to_pack)
pack_all_to(source_folder,destination_folder)
pack_all_to(source_folder,destination_folder,folders_to_pack=folders_to_pack)


# In[ ]:




