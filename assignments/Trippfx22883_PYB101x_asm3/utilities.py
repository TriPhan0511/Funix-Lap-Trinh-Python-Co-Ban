# Sample input:
# 31421250
# Sample ouput:
# 31.461.250
def format_currency(amount):
    return f'{amount:,}'
    # return f'{amount:,}'.replace(',', '.')
