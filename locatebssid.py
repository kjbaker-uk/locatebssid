import urllib.request
import json
import webbrowser

___author___ = 'D4rkc00d3r'

bssid = input('Enter a BSSID: ')  # Mac address of AP you want to locate
api_uri = 'https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid='  # Api endpoint for database.
map_url = 'http://find-wifi.mylnikov.org/#'  # Map provider for plotting results.

# Example of a MAC address; 00:0C:42:1F:65:E9 this can be used for testing.


def mappin():
    while True:
        confirm = input('Show on map? (Y)es or (N)o: ')
        if 'Y' in confirm:
            webbrowser.open(map_url + bssid)
            return
        else:
            break


def results():
    if 'desc' in data:
        print(data['desc'])
    else:
        print('Device has last been seen at:')
        print('Lat: {0}'.format(data['data']['lat']))
        print('Lon: {0}'.format(data['data']['lon']))
        print('Meter accuracy: {0}'.format(data['data']['range']))
        mappin()

# used to write the results of the api call to a .json file.
with urllib.request.urlopen(api_uri + bssid) as url:
    data = json.loads(url.read().decode())
    json_str = json.dumps(data)
    with open('locatebssid.json', 'w') as f:
        json.dump(data, f, indent=4)
        results()
