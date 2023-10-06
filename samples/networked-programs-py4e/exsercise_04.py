# #
# Exercise 4: Change the urllinks.py program to extract and count para-
# graph (p) tags from the retrieved HTML document and display the
# count of the paragraphs as the output of your program. Do not display
# the paragraph text, only count them. Test your program on several
# small web pages as well as some larger web pages.
#


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Get context (Ignore SSL certificate errors)
def get_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def get_tags(url, tag_str):
    ctx = get_context()
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    return soup(tag_str)  # Retrieve all of the tags


def main():
    # url = input('Enter - ')
    url = 'https://docs.python.org'
    print(f'There are {len(get_tags(url, "p"))} paragraphsr in HTML document.')


if __name__ == '__main__':
    main()
