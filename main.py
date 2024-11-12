import json
import csv
from typing import Generator


def read_json_file(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def filter_users(users: list) -> Generator:
    for user in users:
        if (('+1' in user.get('phoneNumber', '') or user.get('phoneNumber', '').startswith('1'))
                and '4.0 Safari' in user.get('userAgent', '')):# Проверка
            yield user['name'], user['address'], user['email']


def write_to_csv(file_path: str,
                 rows: Generator[tuple[str, str, str], None, None]) -> None:
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'address', 'email'])
        writer.writerows(rows)


log_file_path = "in.json"
output_csv_path = "out.csv"

users_data = read_json_file(log_file_path)
filtered_users = filter_users(users_data)
write_to_csv(output_csv_path, filtered_users)

