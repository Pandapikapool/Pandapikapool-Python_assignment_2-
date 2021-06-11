'''
Convert the data stored in question 3 to csv format.
'''

import csv
from collections import OrderedDict

import third

file = third.xmldict

#file = {"spt" : file}

# Function to flatten the nested dictionary

def flatten(d,sep="_"):
    import collections

    obj = collections.OrderedDict()

    def recurse(t,parent_key=""):

        if isinstance(t,list):
            for i in range(len(t)):
                recurse(t[i],parent_key + sep + str(i)
                        if parent_key else str(i))
        elif isinstance(t,dict):
            for k,v in t.items():
                recurse(v,parent_key + sep + k
                        if parent_key else k)
        else:
            obj[parent_key] = t

    recurse(d)

    return obj

# Function to add new row in csv

def add_row(x):
    actor = file['init']['actor'][x]
    result = flatten(actor)
    new_row = list(result.values())
    new_row =  [""] + new_row
    csvwriter.writerow(new_row)


# main Function

csvfile = open('movie.csv', 'w')
csvwriter = csv.writer(csvfile)

result = flatten(file)

first_child = list(result)[0:6]
first_Cvalues = list(result.values())[0:6]
for tag in range(len(first_child)):
    csvwriter.writerow([first_child[tag], first_Cvalues[tag]])

csvwriter.writerow([])

actor = file['init']['actor'][0]


result = flatten(actor)
head_rows = ['init_actor'] + list(result)


csvwriter.writerow(head_rows)

for actors in range(2):
    add_row(actors)



csvfile.close()

