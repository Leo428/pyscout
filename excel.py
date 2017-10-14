
from openpyxl import load_workbook
import json 
fakeInput = "{'teamName':'', 'mode':'', 'total cones':0, 'average cones mbg':0, 'spire':0, 'ground':0, 'mbg time':0, 'cone time':0, 'mbg20':0, 'mbg10':0, 'mbg5':0, 'preload':True}"

wb = load_workbook(filename = 'viewpoint.xlsx')
ws = wb.active
print(wb.get_sheet_names())


json_str = fakeInput.replace("True", "'yes'")
json_str = json_str.replace("'", "\"")
json_str = json_str.replace("\"\"", "\"N/A\"")


print(json_str)
data = json.loads(json_str)
data = [data['teamName'],data['mode'],data['total cones'],data['average cones mbg'],data['spire'],data['ground'],data['mbg time'],data['cone time'],data['mbg20'],data['mbg10'],data['mbg5'],data['preload']]
print(data)
ws.append(data)
wb.save('viewpoint.xlsx')
