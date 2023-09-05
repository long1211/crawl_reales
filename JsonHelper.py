import json
import pandas as pd
from utils.ExcelHelper import write_excel_file

WORK_FLOW = r'sample input/workflow.json'
VIDEO_CALL = r'sample input/video call.json'
MEDIA = r'sample input/media.json'
WORK_FLOW_OUTPUT = r'output//workflow.xlsx'
MEDIA_OUTPUT = r'output//media.xlsx'

output = {}


def read_json_file(filename, sheetname, output_file):
    # Opening JSON file
    f = open(filename)

    # returns JSON object as
    # a dictionary
    output = {}
    data = json.load(f)

    # Iterating through the json
    # list
    path_output = []
    method_output = []
    description_output = []
    paths = data["paths"]
    for path in paths:
        for method in paths[path]:
            method_output.append(method)
            path_output.append(path)
            description_output.append(paths[path][method]['summary'])

    output["Path"] = path_output
    output["Method"] = method_output
    output["Description"] = description_output
    df = pd.DataFrame(output)
    write_excel_file(output_file, sheetname, df)
    # Closing file
    f.close()


read_json_file(WORK_FLOW, 'Workflow', WORK_FLOW_OUTPUT)
# read_json_file(VIDEO_CALL, 'Video Call')
read_json_file(MEDIA, 'Media', MEDIA_OUTPUT)
