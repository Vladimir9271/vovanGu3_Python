import json
import csv


with open('in.json') as file:
    data = json.load(file)

def gen_sqr(number):
   for i in data:
       if i['phoneNumber'][0] == "1" or i['phoneNumber'][0] == "+" and i['phoneNumber'][1] == "1":
           if '4.0 Safari' in i['userAgent']:
               yield i['name'], i['phoneNumber'], i['userAgent']

a = gen_sqr

with open("classmates.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    for i in a(len(data)):
        file_writer.writerow([i])
