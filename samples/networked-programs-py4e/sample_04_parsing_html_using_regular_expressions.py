import os
import re
import urllib.request
import ssl

# #
# Parsing HTML using regular expressions

# One simple way to parse HTML is to use regular expressions to repeatedly search
# for and extract substrings that match a particular pattern.
#


# a_page = '''
# <h1>The First Page</h1>
# <p>
# If you like, you can switch to the
# <a href="http://www.dr-chuck.com/page2.html">
# Second Page</a>.
# </p>
# '''

# pattern = '"(http[s]?://.+?)"'
# lst = re.findall(pattern, a_page)  # ['http://www.dr-chuck.com/page2.html']
# print(lst)

# Our regular expression looks for strings that start with “href="http://” or
# “href="https://”, followed by one or more characters (.+?), followed by another
# double quote. The question mark behind the [s]? indicates to search for the
# string “http” followed by zero or one “s”.

# The question mark added to the .+? indicates that the match is to be done in
# a “non-greedy” fashion instead of a “greedy” fashion. A non-greedy match tries
# to find the smallest possible matching string and a greedy match tries to find the
# largest possible matching string.

# We add parentheses to our regular expression to indicate which part of our matched
# string we would like to extract

# -----------------------------------------------------------

# Sample:
# Search for link values within URL input

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://docs.python.org'
# url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
links = re.findall(b'"(http[s]?://.*?)"', html)
for link in links:
    print(link.decode())

# Output:
# https://docs.python.org/3/index.html
# https://www.python.org/
# http://www.w3.org/2000/svg
# https://www.python.org/doc/versions/
# ...
