import requests
import json
import math
import csv
from lxml.html import fromstring
from itertools import cycle
import traceback
from utils import search
import random


api_key="AIzaSyDh59lQsa5D4Jb2M1Jrahf1HjtQDgl13kw"
num_sites=25


def lambda_handler(event, context):

    query= event["query"]

    proxies = get_proxies()
    
    

    for proxy in proxies:
        try:
            p={"http": proxy, "https": proxy}
            search_result=search(query,3, proxies=p)
            break
        except Exception as e:
            print(e)
            print("Failed Connection trying next")


    response=[ google_to_dict(google) for google in search_result[0:25]]




    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

def google_to_dict(obj):
    properies=[a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj, a))]
    return {key : getattr(obj,key) for key in properies}

def get_proxies():
    url ='https://www.proxy-list.download/api/v1/get?type=https'
    response = requests.get(url)
    urls=response.text.split()
    return urls 
