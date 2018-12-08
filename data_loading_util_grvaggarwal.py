# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 23:01:38 2018

@author: gauraggarwal
"""
# Import Dependencies
import os
import sqlite3
import pandas

print("all dependencies imported")

def dbConnect(client_db):
    """
    Connector for Database
    """
    try:
        db = sqlite3.connect(client_db)
        print(sqlite3.version)
    except sqlite3.Error as e:
        print(e)        
    return db

def getTblNames(source_loc, source_file):
    """
    Read all Table names from the source file
    """
    try:
        with open(os.path.join(source_loc, source_file), "r") as tbl_file:
            all_tbl_names = tbl_file.readlines()
        return all_tbl_names
    except (FileNotFoundError, IOError) as e:
        print("File not found")
    

def getQuery(tbl_name, all_queries):
    """
    Get table relevant query from a dictionary 'all_queries'
    """
    if tbl_name in all_queries.keys():
        query = all_queries[tbl_name]
    else:
        query = "SELECT * from {0}".format(tbl_name)
    return query

def fetchTable(db, tbl_name, query_from, out_loc):
    """
    Query the required table from the Database and return as csv    
    """
    query = getQuery(tbl_name, query_from)
    req_df = pandas.read_sql_query(query, db)
    out_csv = req_df.to_csv(os.path.join(out_loc, tbl_name+".csv"), index = True)
    return out_csv

def main():
    client_db = "client_database.db"
    source_file = r"tables.txt" #file name for txt with all table names
    source_loc = r"..\Input" #source path for tables.txt
    out_loc = r"..\Output" #Output path for csv files
    all_queries = {'TABLE1': "SELECT * from TABLE1"} #dummy dict that includes required queries
    
    db = dbConnect(client_db)
    for tbl_name in getTblNames(source_loc, source_file):
        fetchTable(db, tbl_name, all_queries, out_loc)
    print ("Process Completed") 

if __name__ == '__main__':
    main()
   
    

    
    


