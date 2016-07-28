# -*- coding:utf-8 -*-

import requests
import json

url = 'http://www.lagou.com/jobs/positionAjax.json'

def get_data(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
    data = {
        'first':'false',
        'pn':'2',
        'kd':'Python'
    }
    json_data = requests.post(url,data=data,headers=headers).content.decode('utf-8')

    return json_data

def parse_json(json_data):
    json_obj = json.loads(json_data)
    result = json_obj['content']['positionResult']['result']
    return result

data = parse_json(get_data(url))
for job in data:
    print(job['companyName'],job['city'],job['education'],job['salary'],job['positionType'])


