from services.config import *

def news_api(results):
    response = []
    
    for child in results['articles']:
        response.append({
            'title': child['title'],
            'link': child['url'],
            'source':'newsapi'
        })
    return response

NEWS_API_MAPPING = {
    'api_name':'newsapi',
    'parser':news_api,
    'display_url':'https://newsapi.org/v2/top-headlines?category=general&pageSize={limit}&page=1&'+'apikey={api_key}'.format(api_key=NEWS_API_KEY),
    'search_url':'https://newsapi.org/v2/everything?q={query}&pageSize={limit}&page=1&'+'apikey={api_key}'.format(api_key=NEWS_API_KEY)
    
}
    