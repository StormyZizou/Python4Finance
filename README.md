# Python4Finance
Collaborated effort to learn Python. We will keep track of the problems that have been posed in the README file so that anybody who is included later on in the group has easy documentation to follow:

### Problem 1: Packing Problems
Create the following python functions:
-	pack_it (source_folder): This function takes in a folder path, zips all the subfolders/files and places the zip file in the parent folder (outside the source folder).
-	pack_it_to (source_folder, destination_folder): This function takes two arguments. A source folder path from constituents of which will be zipped and the zip file will be placed in the destination folder. 
-	pack_all (parent_folder, folders_to_pack): This function takes two arguments: a parent folder path and an optional argument that has the list of sub-folders in the parent folder that are to be zipped. All the generated zip files are placed inside the parent folder. If the optional argument list is not provided, all the sub-folders in the parent folder will be zipped and placed in the parent folder. 
-	pack_all_to (parent_folder, folders_to_pack, destination_folder): An extension to the previous function which places all the zip files to a destination folder.

### Problem 2: Data Loading Utility
There is a database system (pick any you know) with various tables containing data to be analyzed. There is also one file (tables.txt) that contains the name of all the tables to be analyzed, with one table name per line. The analysis platform (destination) has a Python SDK that allows user to upload data from a CSV file. Write a Python Utility to support Loading from data in tables to the platform. 