#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd
import numpy as np
import glob
import os

all_data1 = pd.DataFrame()
all_data2 = pd.DataFrame()
src = os.path.abspath(r"C:\Users\bharakumar\Desktop\Loans")
for f in glob.glob(os.path.join(src, 'Loan*.xlsx')):
                   df1 = pd.read_excel(f, sheet_name = "LoanSchedule")
                   df2 = pd.read_excel(f, sheet_name = "Transactions")
                   all_data1 = all_data1.append(df1, ignore_index=True)
                   all_data2 = all_data2.append(df2, ignore_index=True)

writer = pd.ExcelWriter(os.path.join(src, 'Loans_compiled.xlsx'), engine='xlsxwriter')
all_data1.to_excel(writer, sheet_name='LoanSchedule')
all_data2.to_excel(writer, sheet_name='Transactions')

workbook  = writer.book
worksheet = writer.sheets['Transactions']

format1 = workbook.add_format({'bg_color': '#FFEB9C',
                              'font_color': '#9C6500'})

number_rows = len(all_data2.index) + 1

worksheet.conditional_format("$A$1:$AC$%d" % (number_rows),
                             {"type": "formula",
                              "criteria": '=INDIRECT("E"&ROW())="Reversed"',
                              "format": format1
                             }
)

writer.save()


# In[ ]:




