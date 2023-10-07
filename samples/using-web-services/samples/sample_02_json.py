# =============== Parsing JSON ===============

# We construct our JSON by nesting dictionaries and lists as needed. In this example,
# we represent a list of users where each user is a set of key-value pairs (i.e., a
# dictionary). So we have a list of dictionaries.

# In the following program, we use the built-in json library to parse the JSON and
# read through the data. Compare this closely to the equivalent XML data and code
# above. The JSON has less detail, so we must know in advance that we are getting a
# list and that the list is of users and each user is a set of key-value pairs. The JSON
# is more succinct (an advantage) but also is less self-describing (a disadvantage).

import json


data = '''
[
    {
        "id": "001",
        "x": "2",
        "name": "Chuck"
    },
    {
        "id": "009",
        "x": "7",
        "name": "Brent"
    }
]
'''

info = json.loads(data)
print(f'User count: {len(info)}')  # User count: 2

for item in info:
    print(f'ID: {item["id"]}')
    print(f'Name: {item["name"]}')
    print(f'Attribute: {item["x"]}')

# Output:
# ID: 001
# Name: Chuck
# Attribute: 2
# ID: 009
# Name: Brent
# Attribute: 7
