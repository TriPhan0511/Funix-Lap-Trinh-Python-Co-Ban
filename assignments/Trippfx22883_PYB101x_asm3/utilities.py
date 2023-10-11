import ssl
from urllib.request import urlopen
from urllib.error import URLError
import json


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


def get_late_comming_fines(url):
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

    # # Compute number of comments
    # total = 0
    # if 'comments' in res:
    #     comments = res['comments']
    #     for comment in comments:
    #         if 'count' in comment:
    #             try:
    #                 total += int(comment['count'])
    #             except ValueError:
    #                 pass

    # return total
