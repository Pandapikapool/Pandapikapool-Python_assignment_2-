'''
Convert the data stored in question 9 to json format.
'''

import json
import ninth

tag_data = ninth.tag_data

# write in json file
with open('FTX_QA_COLLISIONS.json', 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(tag_data, indent=4))


