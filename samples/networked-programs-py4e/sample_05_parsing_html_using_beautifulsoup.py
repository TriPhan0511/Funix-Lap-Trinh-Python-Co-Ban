
# #
# Parsing HTML using BeautifulSoup
#

# Sample:
# We will use urllib to read the page and then use BeautifulSoup
# to extract the href attributes from the anchor (a) tags.

# The program prompts for a web address, then opens the web page, reads the data
# and passes the data to the BeautifulSoup parser, and then retrieves all of the
# anchor tags and prints out the href attribute for each tag.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# Get context (Ignore SSL certificate errors)
def get_context():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


# Get all specific tags within an url
def get_tags(url, tag_str='a'):
    ctx = get_context()
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    # Retrieve all of the tags
    return soup(tag_str)


# Get links in anchor tags
def get_links(url):
    tags = get_tags(url, 'a')
    result = []
    for tag in tags:
        result.append(tag.get('href', None))
    return result


# Pull out various parts of each tag
def pull_out_various_parts(url):
    tags = get_tags(url, 'a')
    for tag in tags:
        print(f"TAG: {tag}")
        print(f"URL: {tag.get('href', None)}")
        if len(tag.contents) > 0:
            print(f"Contents: {tag.contents[0]}")
        print(f"Attributes: {tag.attrs}")
        print('----------------------------------')


def main():
    # url = input('Enter - ')
    url = 'https://docs.python.org'

    links = get_links(url)
    if len(links) > 0:
        for link in links:
            print(link)

    # pull_out_various_parts(url)


if __name__ == '__main__':
    main()
