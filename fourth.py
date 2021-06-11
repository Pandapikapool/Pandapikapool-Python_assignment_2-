'''
Convert the data stored in question 3 to json format.
'''
# Import parsed data

import json
import third


data = third.xmldict

data = {"spt" : data}
with open('movie.json', 'w') as Jfile:
    json.dump(data, Jfile, indent = 4)



