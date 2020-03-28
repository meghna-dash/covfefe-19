from googlesearch import search as google 
import requests
import json

api_key="AIzaSyDh59lQsa5D4Jb2M1Jrahf1HjtQDgl13kw"

def lambda_handler(event, context):
    print("Event Passed to Handler: " + json.dumps(event))
    
    query= event["query"]

    response={}

    response["toxicity"]=toxicity_analysis(query)
    response["useful-pages"]=search(query)
    response["credibility"]=validity_check(query)








    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
        str1 += ' ' 
    # return string   
    return str1  
        
def search(query):
    return [j for j in google(query , num=5, stop=5)] 

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


def validity_check(query):
    num_sites=20
    credible_sources=0;
    for site in google(query,num=num_sites,stop=num_sites):
        for source in good_sources:
            if source in site.lower():
                credible_sources += 1
                break

    return credible_sources/num_sites
                



good_sources=[
'cdc.gov',
'who.int',
'un.org',
'nih.gov',
'mckinsey.com',
'harvard.edu',
'apha.org',
'avma.org',
'.gov'
]
