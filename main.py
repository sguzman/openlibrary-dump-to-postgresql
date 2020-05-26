import csv
import sys
from typing import Tuple


def load_csv(csv_file: str) -> Tuple[str, str, str, str, str]:
    with open(csv_file) as csv_stuff:
        reader = csv.reader(csv_stuff, delimiter='\t')
        for row in reader:
            type_field: str = row[0]
            work_field: str = row[1]
            num_field: str = row[2]
            date_field: str = row[3]
            json_field: str = row[4].replace("'", "\'")

            new_row: Tuple[str, str, str, str, str] = (type_field, work_field, num_field, date_field, json_field)
            yield new_row


def main() -> None:
    if len(sys.argv) < 2:
        print('Could not find path to ol dump')
        sys.exit()

    csv_file_path: str = sys.arg[1]

    for a, b, c, d, e in load_csv(csv_file_path):
        sql_insert: str = f"INSERT INTO dump (type, about, num, date, data) VALUES ('{a}', '{b}', {c}, '{d}', '{e}');"
        print(sql_insert)


if __name__ == '__main__':
    main()
