'''
Convert the data stored in question 6 to csv format.
'''
# import packages
import json
import csv
import sixth


data = sixth.data
# Function to write in CSV

def writein_csv(data):
    for key in data.keys():
         if key != "runtime_data" and key != "bucketSummaries":
            file.write("%s, %s\n"%(key,data[key]))



runtime_data = data['runtime_data']
bucketSummaries = runtime_data['bucketSummaries']


# Writing in CSV

with open('run_info.csv', 'w') as file:
    writein_csv(data)
    file.write("\nruntime_data \n")
    writein_csv(runtime_data)
    file.write("\nbucketSummaries\n")
    for quailified_name in range(len(bucketSummaries)):
        bucket_data = bucketSummaries[quailified_name]
        writein_csv(bucket_data)
