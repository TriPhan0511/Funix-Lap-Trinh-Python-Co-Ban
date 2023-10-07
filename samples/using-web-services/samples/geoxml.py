from urllib.request import urlopen
from urllib.parse import urlencode
import ssl
import xml.etree.ElementTree as ET

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('\nEnter location: ')  # Sample location: Da nang
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = f'{serviceurl}{urlencode(parms)}'
    print(f'Retrieving {url}')
    data = urlopen(url, context=ctx).read().decode()
    print(f'Retrieved {len(data)} characters.')

    try:
        tree = ET.fromstring(data)
    except:
        tree = None

    if tree is None or tree.find('status') is None or tree.find('status').text != 'OK':
        print('===== Failure To Retrieve =====')
        print(data)
        continue

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    long = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print(f'Latitude: {lat}, Longitude: {long}')
    print(f'Location: {location}')
    # Latitude: 16.0544563, Longitude: 108.0717219
    # Location: Da Nang, Vietnam
