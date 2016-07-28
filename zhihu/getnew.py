#codnig:utf-8

from bs4 import BeautifulSoup
from dologin import login,kill_captcha

session = login('17754113160','inszh123',kill_captcha)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'X-Requested-With' : 'XMLHttpRequest',
}

bs = BeautifulSoup(session.get('https://www.zhihu.com',headers=headers).text,"html.parser")

feed_iter_inner_list = bs.find_all(attrs={'class':'feed-item-inner'})

titleList=[]
for iter in feed_iter_inner_list:
    title = iter.find('h2').getText()
    titleList.append(title)

for t in titleList:
    print(t)

