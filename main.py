import csv
import datetime
import json
import sys
from typing import Dict
from typing import List


class Dump:
    def __init__(self, ttype: str, work: str, num: int, date: datetime.datetime, json: Dict):
        self.type = ttype
        self.work = work
        self.num = num
        self.date = date
        self.json = json

    def __str__(self):
        return f'Dump(\n' \
               f'\tType={self.type},\n' \
               f'\tWork={self.work},\n' \
               f'\tNumber={self.num},\n' \
               f'\tDate={self.date},\n' \
               f'\tJson={json.dumps(self.json, indent=4, sort_keys=True)}\n' \
               f')'


def load_csv(csv_file: str) -> List[Dump]:
    alist: List[Dump] = []

    with open(csv_file) as csv_stuff:
        reader = csv.reader(csv_stuff, delimiter='\t')
        for row in reader:
            type_field: str = row[0].split('/')[-1]
            work_field: str = row[1].split('/')[-1]
            num_field: int = int(row[2])
            date_field: datetime.datetime = datetime.datetime.strptime(row[3], '%Y-%m-%dT%H:%M:%S.%f')
            json_field: Dict = json.loads(row[4].replace("'", "\'"))

            new_row: Dump = Dump(type_field, work_field, num_field, date_field, json_field)
            alist.append(new_row)

    return alist


def main() -> None:
    if len(sys.argv) < 2:
        print('Could not find path to ol dump')
        sys.exit()

    csv_file_path: str = sys.argv[1]

    for d in load_csv(csv_file_path):
        print(d)


if __name__ == '__main__':
    main()
