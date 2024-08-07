"""
განსხვავებულ ფორმატებთან მუშაობა:
- დროსთან და თარიღთან მუშაობა
- მუშაობა Decimal-თან
- რეგულარულ გამოსახულებებთან მუშაობა
- ფაილებთან მუშაობა (მაგალითად csv)
- შეტანა/გამოტანის მოქმედები
- uuid-თან მუშაობა
- os-თან მუშაობა
- კოდირებებთან მუშაობა
"""
import csv
import datetime
import decimal
import json
import os
import re
import time
import uuid


# თარიღები
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

current_time = datetime.datetime.now()
current_timestamp = current_time.timestamp()
in_str = current_time.strftime('%d:%m:%y %H:%M:%S')
in_datetime = datetime.datetime.strptime(in_str, '%d:%m:%y %H:%M:%S')

timestamp = time.time()
from_timestamp = datetime.datetime.fromtimestamp(timestamp)


# Decimal-თან მუშაობა
context = decimal.getcontext()
context.rounding = decimal.ROUND_DOWN

a = decimal.Decimal('0.3')
b = decimal.Decimal(0.3)
c = b.quantize(decimal.Decimal('.0001'), rounding=decimal.ROUND_UP)


# რეგულარულ გამოსახულებებთან მუშაობა
pattern = re.compile(r'^@(\w+)$')
nicknames = ['@qweqwe', '@@qweqwe', 'qweqwe', 'qwe@qwe']
valid_nicknames = [i for i in nicknames if re.match(pattern, i)]


# ფაილებთან მუშაობა
# some_dict = {'qwe': 123}
# file_name = 'new.json'
file_name = 'new.csv'
with open(file_name, 'w') as file:
    # json.dump(some_dict, fp=file, indent=4, ensure_ascii=False)
    fieldnames = ['nicknames', 'length']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for nickname in valid_nicknames:
        writer.writerow({'nicknames': nickname, 'length': len(nickname)})

with open(file_name, 'r') as file:
    # json_obj = json.load(file)
    reader = csv.DictReader(file)
    for row in reader:
        print(row['nicknames'], row['length'])


# შეტანა/გამოტანა
test = input('test:').split()
for i in range(10):
    print(*test, sep='(╯ ° □ °) ╯ ┻━┻', end='\n' + '\t' * i,)


# uuid
uid = uuid.uuid4()


# os
path = os.path.join(__file__, 'qweqwe')
os.getenv('ENV_NAME')

os.system('echo 123')


# Кодировки
a = 'qweqwe'.encode('utf-16')
b = a.decode('utf-16')
