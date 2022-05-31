import traceback
import uvicorn
from fastapi import FastAPI, HTTPException
from services.helpers import *

app = FastAPI()

@app.get('/news')
def list_news(q:str=None,limit:int=10):
    try:
        if q:
            result = news_search(q,limit)
        else:
            result = get_news(limit)
        return result
    except:
        return traceback.print_exc()


if __name__ == '__main__':
    uvicorn.run(app,host='0.0.0.0',port=8000)