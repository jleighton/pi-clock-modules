# -*- coding: utf-8 -*-

import requests
import datetime
import json

dateMMDD = datetime.datetime.now().strftime("%m/%d")
url = 'http://numbersapi.com/' + dateMMDD + '?json'
fact = requests.get(url)

json_data = json.loads(fact.text)

quote = json_data["text"]



print (quote)
