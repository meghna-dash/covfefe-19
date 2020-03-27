from googlesearch import search 
import sys
import requests
import json

api_key="AIzaSyDh59lQsa5D4Jb2M1Jrahf1HjtQDgl13kw"

def main():

    q=sys.argv[1:]

    query=listToString(q)
    print(query)
    toxicity_analysis(query)
    Search(query)

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
        str1 += ' ' 
    # return string   
    return str1  
        
def Search(query):
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
