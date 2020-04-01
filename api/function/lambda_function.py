from .utils.search import search
import requests
import json
import math
import csv 
from lxml.html import fromstring
from itertools import cycle
import traceback



api_key="AIzaSyDh59lQsa5D4Jb2M1Jrahf1HjtQDgl13kw"
num_sites=25


def lambda_handler(event, context):
    
    query= event["query"]

    proxies = get_proxies()
    proxy_pool = cycle(proxies)


    for i in range(1,11):
        #Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d"%i)
        try:
            proxies={"http": proxy, "https": proxy}
            search_result=search(query,3, proxies=proxies)
            break
        except:
            #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
            #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
            print("Skipping. Connnection error")


        response=[ google_to_dict(google) for google in search_result[0:25]]




    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

def google_to_dict(obj):
    properies=[a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj, a))]
    return {key : getattr(obj,key) for key in properies}

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies
