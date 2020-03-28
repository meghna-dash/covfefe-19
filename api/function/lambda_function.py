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