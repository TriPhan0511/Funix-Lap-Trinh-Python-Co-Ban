import ssl
from urllib.request import urlopen
from urllib.error import URLError
import json
import xml.etree.ElementTree as ET
import sys
import os


# Sample input:
# 31421250
# Sample ouput:
# 31,461,250 (VND)
def format_currency(amount):
    return f'{amount:,} (VND)'
    # return f'{amount:,}'.replace(',', '.')


def get_context():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE


def fetch_fines(url):
    # Fetch data from a url
    try:
        ctx = get_context()
        data = urlopen(url, context=ctx).read().decode()
    except URLError:
        print(f'Can not connect to {url}')
        exit()

    # Parse data which has just fetched into a Python dictionary
    try:
        res = json.loads(data)
    except:
        print('===== Failure To Retrieve =====')
        exit()

    # # test
    # print(json.dumps(res, indent=2))

    return res


# Sample fines.json
# [
#   {
#     "min": 0,
#     "max": 3,
#     "value": 20000
#   },
#   {
#     "min": 3,
#     "max": 6,
#     "value": 30000
#   },
#   {
#     "min": 6,
#     "value": 50000
#   }
# ]

# todo: Loop to many times???
def compute_fine(url, late_comming_days):
    fines = fetch_fines(url)
    for d in fines:
        min = d.get('min', 0)
        max = d.get('max', sys.maxsize)
        # max = d.get('max', 31)
        value = d.get('value', 0)

        if late_comming_days <= 0:
            return 0
        if min <= late_comming_days < max:
            fine = late_comming_days * value
            return fine


# Sample tax_rate.xml:
# <taxs>
#     <tax>
#         <min>0</min>
#         <max>5</max>
#         <value>5</value>
#     </tax>
#     <tax>
#         <min>5</min>
#         <max>10</max>
#         <value>10</value>
#     </tax>
#     <tax>
#         <min>10</min>
#         <max>18</max>
#         <value>15</value>
#     </tax>
#     <tax>
#         <min>0</min>
#         <max>5</max>
#         <value>5</value>
#     </tax>
#     <tax>
#         <min>18</min>
#         <max>32</max>
#         <value>20</value>
#     </tax>
#     <tax>
#         <min>32</min>
#         <max>52</max>
#         <value>25</value>
#     </tax>
#     <tax>
#         <min>52</min>
#         <max>80</max>
#         <value>30</value>
#     </tax>
#     <tax>
#         <min>80</min>
#         <value>35</value>
#     </tax>
# </taxs>
def fetch_tax_rates(url):
    # Fetch data from a url
    try:
        ctx = get_context()
        data = urlopen(url, context=ctx).read().decode()
    except URLError:
        print(f'Can not connect to {url}')
        exit()

    # Parse data which has just fetched and compute numbers of comments
    tree = ET.fromstring(data)
    mins = tree.findall('tax/min')
    maxes = tree.findall('tax/max')
    values = tree.findall('tax/value')

    # todo
    # Use try..exept
    mins = [int(i.text) for i in mins]
    maxes = [int(i.text) for i in maxes]
    values = [int(i.text) for i in values]

    return (mins, maxes, values)


def compute_tax(url, amount):
    tax_rates = fetch_tax_rates(url)
    amount = amount / 1000000
    mins, maxes, values = tax_rates
    for i in range(1, len(mins)):
        min = mins[i]
        value = values[i]
        try:
            max = maxes[i]
        except IndexError:
            max = sys.maxsize
            # max = 8000

        if amount <= 0:
            return 0
        if min <= amount < max:
            return value / 100 * amount * 1000000


def get_full_path(file_name):
    # This function returns the path of the file
    absolute_path = os.path.dirname(__file__)
    return f'{absolute_path}/{file_name}'


# Write a list of custom objects (example: list of Employee objects) to a json file
# Sample list:
# lst = [
#         Department('SALE001', 300000),
#         Department('SALE002', 400000)
#     ]
def write_list(lst, fhand):
    try:
        # json.dumps(): Serialize a Python object into a JSON string
        lst = [json.dumps(obj.__dict__) for obj in lst]
        fhand.write('[\n')
        for i in range(len(lst)):
            item = lst[i]
            if i == len(lst) - 1:
                fhand.write(f'\t\t{item}\n')
            else:
                fhand.write(f'\t\t{item},\n')
        fhand.write('\t')
        fhand.write(']')
    except Exception as err:
        print(err)
        return False
    return True


# Write a Python dictionary to a json file
# The values in the dictionary are lists of custom objects(Department objects, Employee objects...)

# Sample dictionary:
# d = {
#         'departments': departments,
#         'employees': employees
# }

# Sample output file:
# {
# 	"departments": [
# 		{"id": "ACCOUNTING", "bonus_salary": 450000},
# 		{"id": "MARKETING", "bonus_salary": 1000000},
# 		{"id": "IT", "bonus_salary": 650000},
# 		{"id": "SALE001", "bonus_salary": 500000},
# 		{"id": "SALE002", "bonus_salary": 550000}
# 	],
# 	"employees": [
# 		{"id": "NV001", "name": "John Doe", "salary_base": 200000, "working_days": 26, "department": "ACCOUNTING", "working_performance": 1, "bonus": 500000, "late_comming_days": 0},
# 		{"id": "NV002", "name": "Rose Mary", "salary_base": 200000, "working_days": 26, "department": "SALE002", "working_performance": 1, "bonus": 500000, "late_comming_days": 0, "is_manager": true}
# 	]
# }
def write_data_to_file(file_name, d):
    keys = list(d.keys())
    values = list(d.values())
    try:
        fhand = open(get_full_path(file_name), 'w')
        fhand.write('{' + '\n')
        for i in range(len(keys)):
            fhand.write(f'\t{json.dumps(keys[i])}: ')
            if i == len(keys) - 1:
                write_list(values[i], fhand)
            else:
                write_list(values[i], fhand)
                fhand.write(',\n')
        fhand.write('\n}')
        fhand.close()
    except Exception as err:
        print(err)
        return False
    return True


# Read from a json file and return a Python dictionary
# which contains a list of Department objects and a list of Employee objects.
def read_json_file(file_name):
    try:
        fhand = open(get_full_path(file_name))
        data = fhand.read()
        if len(data) == 0:
            return None
    except FileNotFoundError:
        print(f'Can not open file {file_name}')
        return None
    try:
        # Parse a JSON string into a Python object
        result = json.loads(data)
    except Exception as err:
        print(err)
        return None
    return result


# Display departments or employees
def display_list(lst, msg='===== Display list =====', empty_msg='Empty list'):
    print(msg)
    if len(lst) == 0:
        print(empty_msg)
    for item in lst:
        print(f'{item}\n')
