import requests

def reddit_api(results):
    response = []
    
    for child in results['data']['children']:
        response.append({
            'title': child['data']['title'],
            'link': child['data']['url'],
            'source':'reddit'
        })
    return response

REDDIT_API_MAPPING = {
    'api_name':'reddit',
    'parser':reddit_api,
    'display_url':('http://www.reddit.com/r/news/top.json?''limit={limit}'),
    'search_url':('http://www.reddit.com/r/news/search.json?''q={query}&limit={limit}')
    
}
    