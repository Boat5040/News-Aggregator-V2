from .APIs.news import *
from .APIs.reddit import *

API_COLLECTION = [
    NEWS_API_MAPPING,
    REDDIT_API_MAPPING
]

def verify_parser(response):
    required_fields =['title','link','source']
    return None

def get_news(limit):
    response =[]
    for api in API_COLLECTION:
        result = requests.get(api['display_url'].format(limit=limit),headers={'User-agent':'your bot 0.1'}).json()
        if result:
            response+=api[']'](result)
    return response

def news_search(query, limit):
    response = []
    for api in API_COLLECTION:
        result = requests.get(api['search_url'].format(query=query, limit=limit),headers={'User-agent':'your bot 0.1'}).json()
        if result:
            response+=api['parser'](result)
    return response
