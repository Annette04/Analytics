import datetime
import requests
import json
import pandas as pd

def getPage(page, params):
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.content.decode()
    req.close()
    return data


for page in range(0, 1):
    params = {
        'text': 'NAME:Android',
        'per_page': 100
    }
    params1 = {
        'text': 'NAME:Андроид',
        'per_page': 100
    }
    jsObj = json.loads(getPage(page, params))
    jsObj1 = json.loads(getPage(page, params1))
    df = pd.DataFrame(jsObj['items'])
    df1 = pd.DataFrame(jsObj1['items'])
    res = pd.concat([df, df1], join='outer', ignore_index=True).sort_values(by='published_at', ascending=False)
    date = (datetime.datetime.now()-datetime.timedelta(1)).strftime('%Y-%m-%dT%H:%M:%S')
    res = res[res['published_at'] >= date].head(10)
    if (jsObj['pages'] - page) <= 1:
        break
