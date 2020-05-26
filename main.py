import csv
from typing import Tuple


csv_file: str = './ol_dump_works_2020-04-30_25_entries.csv'


def load_csv() -> Tuple[str, str, str, str, str]:
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
    for a, b, c, d, e in load_csv():
        print(a, b, c, d, e)


if __name__ == '__main__':
    main()
