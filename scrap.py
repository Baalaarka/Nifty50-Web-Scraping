from helpers import rds
import requests
import json


url = "https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json"


def scrap_data():
    try:
        req = requests.get(url)
        data = req.json().get('data')
        print data
        rds.set("nif_top_ten", json.dumps(data))
    except Exception as e:
        print e.message
        print 'Could not scrape data'
