'''
Parse the attached csv file, store it as a suitable data structure(list, set, tuple,
dictionary and class)
'''
import csv
import pprint
from csv import reader

# main code
with open('FTX_QA_COLLISIONS.csv', 'r') as file:
    next(file)
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)
    tag_data = { 'Report for tag: FTX_QA_COLLISIONS' : data}

with open('FTX_QA_COLLISIONS.csv', 'r') as file:
    csv_reader = reader(file)
    edata = list(csv_reader)

pprint.pprint(tag_data)

