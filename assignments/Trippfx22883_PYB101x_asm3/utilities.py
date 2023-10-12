import ssl
from urllib.request import urlopen
from urllib.error import URLError
import json
import xml.etree.ElementTree as ET
import sys


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
        res = None

    if res is None:
        print('===== Failure To Retrieve')
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
            # test
            # print(min, max, value / 100)
            return value / 100 * amount * 1000000


# def compute_bonus_salary(emp, depts):
#     lst = [(dept.id, dept.bonus_salary) for dept in depts]
#     dept_id = emp.department
#     for id, bonus_salary in lst:
#         if id == dept_id:
#             if isinstance(emp, Manager):
#                 return bonus_salary + bonus_salary * 0.1
#             return bonus_salary


def main():
    # # test compute_fine(url, late_comming_days)
    # url = 'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de'
    # for late_comming_days in range(10):
    #     fine = compute_fine(url, late_comming_days)
    #     print(f'fine={format_currency(fine)}\n')
    # -----------------------------------------------------------------------

    # # test fetch_tax_rate(url) function
    # url = 'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7'
    # tax_rates = fetch_tax_rates(url)
    # # mins, maxes, values = tax_rates
    # # # [0, 5, 10, 0, 18, 32, 52, 80]
    # # # [5, 10, 18, 5, 32, 52, 80]
    # # # [5, 10, 15, 5, 20, 25, 30, 35]
    # -----------------------------------------------------------------------

    # test compute_tax(url, amount) function
    url = 'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7'
    amounts = [0, 500000, 2000000, 4999999,
               5000000, 9999999, 80000000, 100000000]
    for amount in amounts:
        # print(f'amount={format_currency(amount)}')
        # print(f'amount2={format_currency(amount/1000000)}')
        tax = compute_tax(url, amount)
        print(f'tax={format_currency(tax)}')
        print('--------------')


if __name__ == '__main__':
    main()
