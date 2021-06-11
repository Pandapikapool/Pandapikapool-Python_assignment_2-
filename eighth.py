# import packages

from xlwt import Workbook
import sixth

data = sixth.data

# Function to write in xlsx

def writein_sheet(sheet, data ,row, col):
    row
    for key in data.keys():
        if key != "runtime_data" and key != "bucketSummaries":
            sheet.write(row, col, key)
            sheet.write(row, col + 1, '%s' %data[key])
            row += 1
    return(row,col+1)



runtime_data = data['runtime_data']
bucketSummaries = runtime_data['bucketSummaries']

wb = Workbook()

# Write in excel sheet
row, col = 0,0

sheet1 = wb.add_sheet('system_config')
row, col = writein_sheet(sheet1, data, row, col)
sheet1.write(row, 0, "runtime_data")
row, col = writein_sheet(sheet1, runtime_data, row, col)

sheet1.write(row,col-1, "bucketSummaries")
row += 1

sheet1.write(row, col, 'qualifiedName')
sheet1.write(row, col + 1, 'hits')
row += 1


for quailified_name in range(len(bucketSummaries)):
    bucket_data = bucketSummaries[quailified_name]
    sheet1.write(row, col, bucket_data['qualifiedName'])
    sheet1.write(row, col+1, '%s' %bucket_data['hits'])
    row += 1

wb.save('run_info.xls')



