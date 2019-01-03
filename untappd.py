# -*- coding: utf-8 -*-

import requests
import json
import secrets


url = 'https://api.untappd.com/v4/user/checkins/' + secrets.untappd_username + '?client_id=' + secrets.untappd_clientid + '&client_secret=' + secrets.untappd_secret
untappd = requests.get(url)
json_data = json.loads(untappd.text)
#load the json structure
LatestBeers = json_data["response"]["checkins"]

#go to the items key and pick the top one
LatestBeers = LatestBeers["items"][0]

print (LatestBeers.keys())

LatestBeer = (LatestBeers["beer"]["beer_name"])
LatestBrewery = (LatestBeers["brewery"]["brewery_name"])

LatestRating = (LatestBeers["rating_score"])
LatestDate = (LatestBeers["created_at"])
LatestVenue = (LatestBeers["venue"]["venue_name"])
LatestComment = (LatestBeers["checkin_comment"])
LatestToasts = (LatestBeers["toasts"]["total_count"])

print ("%s by %s at %s" % (LatestBeer, LatestBrewery, LatestVenue))
print ("Rating: %s/5" % LatestRating)
print ("Date: %s" % LatestDate)
print ("Comment: %s" % LatestComment)
print ("Toasted %s times" % LatestToasts)
