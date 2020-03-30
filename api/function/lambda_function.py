from google import google
import requests
import json
import math
import csv 


api_key="AIzaSyDh59lQsa5D4Jb2M1Jrahf1HjtQDgl13kw"
num_sites=25


def lambda_handler(event, context):
    
    query= event["query"]

    search_result=google.search(query,3)
    response=[ google_to_dict(google) for google in search_result[0:25]]
    
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

def google_to_dict(obj):
    properies=[a for a in dir(obj) if not a.startswith('__') and not callable(getattr(obj, a))]
    return {key : getattr(obj,key) for key in properies}





def scale(x):
    x=math.tanh(4*x)
    
    return x

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
        str1 += ' ' 
    # return string   
    return str1  
        
def toxicity_analysis(query):
    url = ('https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze' + '?key=' + api_key)
    data_dict = {
        'comment': {'text': query},
        'languages': ['en'],
        'requestedAttributes': {'TOXICITY': {}}
    }
    response = requests.post(url=url, data=json.dumps(data_dict))
    response_dict = json.loads(response.content)
    return response_dict["attributeScores"]["TOXICITY"]["summaryScore"]["value"]




def neg_validity_check(results):
    credible_sources=0
    for site in results:
        for source in bad_sources:
            if source in site.lower():
                credible_sources += 1 
                break
    
    return credible_sources/num_sites

def med_validity_check(results):
    credible_sources=0
    for site in results:
        for source in good_sources:
            if source in site.lower():
                credible_sources += 1 
                break
    
    return credible_sources/num_sites
 

def news_validity_check(results):
    credible_sources=0
    for site in results:
        for source in news_sources.keys():
            if source in site.lower():
                credible_sources+=news_sources[source]

    return credible_sources/(num_sites*3)
    



good_sources=[
'cdc.gov',
'who.int',
'un.org',
'nih.gov',
'mckinsey.com',
'harvard.edu',
'apha.org',
'avma.org',
'.gov',
'.edu',
'hopkinsmedicine.org'
]

bad_sources=json.load(open('data/bad_sites.txt'))

news_sources=json.load(open('data/news_urls.json'))
