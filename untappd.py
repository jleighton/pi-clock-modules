# -*- coding: utf-8 -*-

import requests
import json
import secrets

url = 'https://api.untappd.com/v4/user/checkins/' + secrets.untappd_username + '?client_id=' + secrets.untappd_clientid + '&client_secret=' + secrets.untappd_secret
untappd = requests.get(url)
json_data = json.loads(untappd.text)

LatestBeers = json_data["response"]["checkins"]


#LatestBeer = json_data["count"]["items"]

#print (LatestBeer.keys())

#LatestBeerNames = json_data["items"]["0"]

#print (LatestBeerName)
