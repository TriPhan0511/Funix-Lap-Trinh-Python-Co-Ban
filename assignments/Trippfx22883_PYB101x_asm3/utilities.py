import ssl
from urllib.request import urlopen
from urllib.error import URLError
import json
from functools import reduce


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
def compute_fine(lst, late_comming_days):
    for d in lst:
        min = d.get('min', 0)
        max = d.get('max', 31)
        value = d.get('value', 0)

        if late_comming_days <= 0:
            # # test
            # print(f'late_comming_days={late_comming_days} fine={0}')
            return 0
        if min <= late_comming_days < max:
            fine = late_comming_days * value
            # # test
            # print(
            #     f'late_comming_days={late_comming_days} value={value} fine={fine}')
            return fine


def main():
    url = 'https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de'
    lst = fetch_fines(url)
    for late_comming_days in range(8):
        fine = compute_fine(lst, late_comming_days)
        print(f'fine={fine}\n')


if __name__ == '__main__':
    main()
