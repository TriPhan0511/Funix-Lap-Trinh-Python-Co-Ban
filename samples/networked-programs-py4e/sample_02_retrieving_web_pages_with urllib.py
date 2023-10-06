import urllib.request

# #
# Retrieving web pages with urllib (text files)

# Using urllib, you can treat a web page much like a file. You simply indicate
# which web page you would like to retrieve and urllib handles all of the HTTP
# protocol and header details.
#


# Sample:
# Retrieve the data for romeo.txt and compute the frequency of each word in the file.

def compute_frequency(url):
    try:
        fhand = urllib.request.urlopen(url)
    except ValueError:
        print(f'Can not acces to {url}.')
        exit()
    d = {}
    for line in fhand:
        words = line.decode().strip().split()
        for w in words:
            w = w.lower()
            d[w] = d.get(w, 0) + 1
    return d


def arrange(d):
    lst = []
    for k, v in d.items():
        lst.append((v, k))
    lst.sort(reverse=True)
    return lst


def main():
    url = 'http://data.pr4e.org/romeo.txt'
    d = compute_frequency(url)
    lst = arrange(d)
    print('\nFrequency of words:\n')
    for (x, y) in lst:
        print(f'{y}: {x} time(s)')


if __name__ == '__main__':
    main()
