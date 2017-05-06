# Introduction
LocateBIID is a simple tool made in Python3 to check the location of an Access Point MAC address from a opensource database.

## Why I made it?
I am learning how to use Application Programming Interface (API) within Python and how to handle the returned data in json.

## What can locatebssid do?
with locatebssid you are able to enter a MAC address and make a api request to get the location of the BSSID providing it
is in the database. If the BSSD is in the database it will print out the Lat/Lon and give you the option to view it in Google
Maps as a pin.

## What does the json result look like?
The json below is returned from the api provider and I add some formatting to make it readable.

```json
  {
    "result": 200,
    "data": {
        "time": 1494088927,
        "lon": 16.54751061246,
        "lat": 45.21966319365,
        "range": 132.926
    }
}
```
example based on the test BSSID of 00:0C:42:1F:65:E9

## What API am I using and why?
I am using the opensource WiFi data base of https://www.mylnikov.org/ made by ALEXANDER MYLNIKOV. I started googling for
a public WiFi database and found his. I choose it as it dose not require a API Key or have a request limit so it is great
for a first time API. It has over 35 million worldwide records in it apparently.

## How to use locatebssid?
Simply clone or download the script locatebssid project and make the script executable with the following command;

```
sudo chmod +x locatebssid.py
```
then to run bssid simply type;
```
python3 locatebssid.py
```
Below is an example of the console output.
![sceenshot_console](https://cloud.githubusercontent.com/assets/17799879/25775477/b07bba92-329d-11e7-8683-0d0f80c55394.png)

If you select Y at the option it will open the browser to locate the BSSID.
![map1](https://cloud.githubusercontent.com/assets/17799879/25775497/ebc9bd2e-329d-11e7-8621-6c2c5aa4d68e.png)

## Additional notes
1. Each time you ru the script check the locatebssid.json file to see it change.
2. I have tried to make it as clean as possable adhering to PEP 8.

## Credits
The API and lookup website belongs to ALEXANDER MYLNIKOV at https://www.mylnikov.org/
