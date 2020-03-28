from googlesearch import search 
import requests
import json

api_key="AIzaSyDh59lQsa5D4Jb2M1Jrahf1HjtQDgl13kw"

def lambda_handler(event, context):
    print print_function('Function Executing')
    print("Event Passed to Handler: " + json.dumps(event))
    









    return {
        'statusCode': 200,
        'body': json.dumps(event)
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
    for j in search(query , num=5, stop=5): 
        print(j) 

def toxicity_analysis(query):
    url = ('https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze' + '?key=' + api_key)
    data_dict = {
        'comment': {'text': query},
        'languages': ['en'],
        'requestedAttributes': {'TOXICITY': {}}
    }
    response = requests.post(url=url, data=json.dumps(data_dict))
    response_dict = json.loads(response.content)
    print(f'Toxicity Level:{response_dict["attributeScores"]["TOXICITY"]["summaryScore"]["value"]}')

main()
