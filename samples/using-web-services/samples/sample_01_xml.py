import xml.etree.ElementTree as ET
from utilities import get_full_path

# =============== Parsing XML ===============

# # data2 = open(get_full_path('person.xml')).read()

# data = '''
# <person>
#     <name>Chuck</name>
#     <phone type="intl">
#         +1 734 303 4456
#     </phone>
#     <email hide="yes" />
# </person>'''


# tree = ET.fromstring(data)
# print(f"Name: {tree.find('name').text}")
# print(f"Attr: {tree.find('email').get('hide')}")
# # Output:
# # Name: Chuck
# # Attr: yes

# =============== Looping through nodes ===============

# Often the XML has multiple nodes and we need to write a loop to process all of
# the nodes. In the following program, we loop through all of the user nodes:

input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>
'''

# stuff = ET.fromstring(input)

# lst = stuff.findall('users/user')
# print(f'User count: {len(lst)}')
# if len(lst) > 0:
#     for user in lst:
#         print(f"ID: {user.find('id').text}")
#         print(f"Name: {user.find('name').text}")
#         print(f"Attribute: {user.get('x')}")

# # Output:
# # User count: 2
# # ID: 001
# # Name: Chuck
# # Attribute: 2
# # ID: 009
# # Name: Brent
# # Attribute: 7

# Notes:
# It is important to include all parent level elements in the findall statement except
# for the top level element (e.g., users/user). Otherwise, Python will not find any
# desired nodes.

# -----------------------------------------------------------

stuff = ET.fromstring(input)

lst = stuff.findall('user/users')
print(f'User count: {len(lst)}')  # 2

lst2 = stuff.findall('users')
print(f'User count: {len(lst2)}')  # 0

# lst stores all user elements that are nested within their users parent. lst2 looks
# for user elements that are not nested within the top level stuff element where
# there are none.
