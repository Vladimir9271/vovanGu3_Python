import json
import csv

def reading_file(log_file):
    with open(log_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in data:
            # Проверка на принадлежность к США и использование Safari 4.0
            if ('+1' in i.get('phoneNumber', '') or i.get('phoneNumber', '').startswith('1')) and '4.0 Safari' in i.get('userAgent', ''):
                print(i)
                yield i['name'], i['address'], i['email']


def write_to_csv(output_file, generator):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'address', 'email'])  # заголовок
        writer.writerows(generator)  # запись данных из генератора


generator = reading_file("in.json")
write_to_csv("out.csv", generator)
