import json
import os
import datetime

#This is a library full of functions related to data retrieval

def grabJSONifExists(path, default_dict=None):
    if os.path.isfile(path):
        with open(path, 'r') as f:
            return json.load(f)

    else:
        writeJSONtoPath(path, default_dict)
        return default_dict

def writeJSONtoPath(path, dict_in):
    with open(path, 'w') as f:
        json.dump(dict_in, f)

def generateReport(path, report_list):
    default_dict = {}
    report = grabJSONifExists(path, default_dict)

    report[str(datetime.date.today())] = report_list
    writeJSONtoPath(path, report_list)
    return report