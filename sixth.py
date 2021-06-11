'''
Parse the attached json file, store it as a suitable data structure(list, set, tuple,
dictionary and class)
'''

# importing the module
import json


with open('run_info.json', 'r') as Jfile:
    data = json.load(Jfile)
    print(json.dumps(data, indent = 4))
    

