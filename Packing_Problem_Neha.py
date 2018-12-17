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
    '''Creates zip file for each of the folders/directories present in the source folder'''
    Full_dir_list=os.listdir() #List of files and directories/folders in the source folder
    zip_folder_path=[]
    suffix='.zip'
    for i, j in enumerate(Full_dir_list):
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
    '''Creates zip file for each of the folders/directories present in the source folder and move them to the 
    desired destination folder'''
    Full_dir_list=os.listdir() #List of files and directories/folders in the source folder
    zip_folder_path=[]
    suffix='.zip'
    for i, j in enumerate(Full_dir_list):
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
    '''Creates seperate zip file for all or specific folders/directories present in the source folder'''
    zip_folder_path=[]
    suffix='.zip'
    if (folders_to_pack==None):
        list_to_iterate= os.listdir() #List of all files and directories/folders in the source folder
    else:
        list_to_iterate= folders_to_pack # List of the folders to pack
    
    for i,j in enumerate(list_to_iterate):
            zip_folder_path=os.path.join(source_folder,list_to_iterate[i]) #Path for each file or folder in the source folder
            if os.path.isdir(zip_folder_path): #Packs only folders and not files
                if os.path.isfile(os.path.join(source_folder,list_to_iterate[i]+suffix)): #Check if the zip file already exists in the source folder
                    File_Name= list_to_iterate[i]+suffix
                    print(File_Name,'already exists')
                else:
                    shutil.make_archive(list_to_iterate[i],'zip', zip_folder_path)  #Creates the zip file


# In[397]:


#Packs all the folders in the source folder or the specific folders and move them to destination folder
def pack_all_to(source_folder,destination_folder,folders_to_pack=None):
    '''Creates seperate zip file for all or specific folders/directories present in the source folder and move them to the desired 
    destination folder'''
    zip_folder_path=[]
    suffix='.zip'
    if (folders_to_pack==None):
        list_to_iterate= os.listdir() #List of all files and directories/folders in the source folder
    else:
        list_to_iterate= folders_to_pack # List of the folders to pack
        
    for i,j in enumerate(list_to_iterate):
            zip_folder_path=os.path.join(source_folder,list_to_iterate[i]) #Path for each file or folder in the source folder
            if os.path.isdir(zip_folder_path): #Packs only folders and not files
                if os.path.isfile(os.path.join(destination_folder,list_to_iterate[i]+suffix)): #Check if the zip file already exists in the destination folder
                    File_Name= list_to_iterate[i]+suffix
                    print(File_Name,'already exists')
                    if os.path.isfile(os.path.join(source_folder,list_to_iterate[i]+suffix)): #Check if the zip file already exists in the source folder and delete it
                        os.remove(os.path.join(source_folder,list_to_iterate[i]+suffix))
                else:
                    shutil.make_archive(list_to_iterate[i],'zip', zip_folder_path) #Creates the zip file
                    shutil.move(zip_folder_path+suffix,destination_folder) #Move the zip file to destination folder


# In[410]:

def main():
    '''Create and move zip files from one folder to another based on requirement'''
    
    Desired_directory= r'C:\Users\ndandu\Desktop\citi\Non FRTB Pricing Model\TestFX' #Checking if the current working directory is same as the desired directory

    if os.getcwd()!=Desired_directory:
         os.chdir(Desired_directory)
           
    source_folder= os.getcwd() #Setting the source folder to desired working directory 
   
    destination_folder=r'C:\Users\ndandu\Desktop\citi\Non FRTB Pricing Model\TestFx2'  #Defining the destination folder

    folders_to_pack=['156363'] #List of folders to pack
    
    pack_it(source_folder)
    pack_it_to(source_folder,destination_folder)
    pack_all(source_folder)
    pack_all(source_folder,folders_to_pack=folders_to_pack)
    pack_all_to(source_folder,destination_folder)
    pack_all_to(source_folder,destination_folder,folders_to_pack=folders_to_pack)
    
if __name__=="__main__":
    main()   

# In[ ]:




