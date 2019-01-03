# -*- coding: utf-8 -*-

import requests
import json
import secrets

url = 'https://api.darksky.net/forecast/' + secrets.dark_sky_secret_key +'/'+ secrets.dark_sky_latlong +'?units=auto&exclude=minutely,alerts,flags'
weather = requests.get(url)
json_data = json.loads(weather.text)

temp = json_data["currently"]["temperature"]
feelslike = json_data["currently"]["apparentTemperature"]
summary = json_data["hourly"]["summary"]

print ("Current Temperature: %s°C (Feels like %s)" % (temp, feelslike) )
print ("Current Summary: %s" % summary)
