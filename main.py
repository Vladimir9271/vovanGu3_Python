import json

with open('in.json') as file:
    data = json.load(file)

for text in data:
    if text['phoneNumber'][0]=="1" or text['phoneNumber'][0]=="+" and text['phoneNumber'][1]=="1":
         if '4.0 Safari' in text['userAgent']:
            print(text['name'] ,"  " ,text['phoneNumber'],"  ", text['userAgent'])

# print(json.dumps(data, indent=4))