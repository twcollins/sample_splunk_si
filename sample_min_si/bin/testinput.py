
from __future__ import print_function
import requests
import json
from time import localtime,strftime




url = "API URL"
# API headers 
headers = { }


resp = requests.get(url, verify=False, headers=headers)

flatten_dimensions_metrics = {}
results = []

jsondata = resp.json()

indexTime = "[" + strftime("%m/%d/%Y %H:%M:%S %p %Z", localtime()) + "]"

# flatten the data result and output as a combined event
for row in jsondata['result']['data']:

    flatten_dimensions_metrics = {
        # dimensions
        'queryName' :  row['dimensions'][0],
        'queryType' : row['dimensions'][1],
        'responseCode' : row['dimensions'][2],
        'responseCached' : row['dimensions'][3],
        'coloName' : row['dimensions'][4],
        'origin' : row['dimensions'][5],
        'dayOfWeek' : row['dimensions'][6],
        'tcp' : row['dimensions'][7],
        'ipVersion' : row['dimensions'][8],
        'querySizeBucket' : row['dimensions'][9],
        'responseSizeBucket' : row['dimensions'][10],
        #metrics
        'queryCount' : row['metrics'][0],
        'uncachedCount'  : row['metrics'][1],
        'staleCount' : row['metrics'][2],
        'responseTimeAvg' :  row['metrics'][3]
    }

    print("%s %s" % (indexTime,         ", ".join(["=".join([key, str(val)]) for key, val in flatten_dimensions_metrics.items()])))

