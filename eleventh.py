'''
Convert the data stored in question 9 to excel format.
'''

# import packages

from csv import reader
import ninth
import xlwt
from xlwt import Workbook

# Writing in excel sheet

data = ninth.edata
wb = Workbook()
sheet1 = wb.add_sheet('Report')

sheet1.write(0, 0, data[0])

for rows in range(1,len(data)):
    for fields in range(len(data[rows])):
        sheet1.write(rows, fields, data[rows][fields])


wb.save('FTX_QA_COLLISIONS.xls')

