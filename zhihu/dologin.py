# -*- coding:utf-8 -*-

import time
import requests
import json
from bs4 import BeautifulSoup

def login(username, password, oncaptcha):
    session = requests.session()

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    _xsrf = BeautifulSoup(session.get('https://www.zhihu.com/#signin',headers=headers).text,"html.parser").find('input',attrs={'name': '_xsrf'})['value']
    captcha_content = session.get('http://www.zhihu.com/captcha.gif?r=%d' % (time.time() * 1000),headers=headers).content
    data = {
        '_xsrf': _xsrf,
        'phone_num': username,
        'password': password,
        'captcha_type':'cn',
        'remember_me':'true',
        'captcha': oncaptcha(captcha_content)
    }

    resp = session.post('https://www.zhihu.com/login/phone_num',headers=headers,data=data).text
    # assert b'\\u767b\\u5f55\\u6210\\u529f' in resp #登陆成功
    resp_dic = json.loads(resp)
    name = BeautifulSoup(session.get('https://www.zhihu.com', headers=headers).text, "html.parser").find('span', attrs={
        'class': 'name'}).getText()
    print(name,resp_dic['msg'])
    return session

def kill_captcha(data):
    with open('captcha.png','wb') as fp:
        fp.write(data)
    return input('captcha: ')

if __name__ == '__main__':
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    session= login('17754113160','inszh123',kill_captcha)
    name = BeautifulSoup(session.get('https://www.zhihu.com',headers=header).text,"html.parser").find('span',attrs={'class':'name'}).getText()
    print(name)
