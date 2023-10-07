from urllib.request import urlopen
from urllib.parse import urlencode
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    # Sample input: Da nang
    # Sample input: Ann Arbor, MI

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
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('===== Failure To Retrieve =====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    long = js['results'][0]['geometry']['location']['lng']
    location = js['results'][0]['formatted_address']

    print(f'Latitude: {lat}, Longitude" {long}')
    print(f'Location: {location}')
    # Latitude: 16.0544563, Longitude" 108.0717219
    # Location: Da Nang, Vietnam
