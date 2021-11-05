# -*- coding: utf-8 -*-

# -- Sheet --

#print out shortName, regulrmarketprice, and regularMarketTime convertde to a reddable time
#save symbol, regularMarketTime, and regularMarketprice to a csv
#add to csv file when you rub it

import datetime
import csv
import requests

apikey='FIADZrUhDV79nXLRp6fMtu41VaM8qi91tsQKrnS4'

url = "https://yfapi.net/v6/finance/quote"

#get desired name

print('Please enter name of stock ticker:')
x = input()
if len(x) != 4:
    print('Not a known stock ticker')
else:
    print('Retriving ' + x)

querystring = {"symbols": x}

headers = {
    'x-api-key': apikey
    }

response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

# response.raise_for_status()  # raises exception when not a 2xx response
# if response.status_code != 204:
#    stock_json = response.json()
#    print(stock_json['quoteResponse']['result'][0]["displayName"] + " Price:$" + str(stock_json['quoteResponse']['result'][0]["regularMarketPrice"]))


#extracting elements I need
dict1 =response.json()
# print(dict1)

keys_to_extract = ["symbol", "regularMarketPrice", 'regularMarketTime']

dict2 = {key: dict1['quoteResponse']['result'][0][key] for key in keys_to_extract}




#converting time
tm = int(dict2.get('regularMarketTime'))
datetime_time = datetime.datetime.fromtimestamp(tm)
dict2["regularMarketTime"] = datetime_time

print('The company short name is ' , dict2["symbol"])
print('The regular market price name is ' , dict2["regularMarketPrice"])
print('The regular market time is ' , dict2["regularMarketTime"])


#writing output to file
f = open('output.csv', 'w')
writer = csv.writer(f)
for key, value in dict2.items():
    writer.writerow([key,value])
f.close()



