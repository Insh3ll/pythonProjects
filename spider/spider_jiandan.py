# coding:utf-8

import requests
from bs4 import BeautifulSoup


desturl = 'http://jandan.net/ooxx/'

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36',
}


def parse_html(html):
    sp = BeautifulSoup(html)
    ol_list = sp.find('ol', attrs={'class': 'commentlist'})
    img_list = []

    for li in ol_list.find_all('li'):
        img_link = li.find('a',attrs={'class': 'view_img_link'})['href']
        img_list.append(img_link)

    next_page = sp.find('a', attrs={'class': 'previous-comment-page'})['href']
    if next_page:
        return img_list, next_page

    return img_list, None


def down_pic(img_link):
    print(img_link)
    pic_name = img_link.split('/')[-1]
    content = requests.get(img_link, headers=headers).content
    with open('pic/'+pic_name, 'wb') as f:
        f.write(content)

def get_html(url):
    return requests.get(dest_url, headers=headers).text


if __name__ == '__main__':
    next_page = dest_url
    for i in range(50):
        html = get_html(next_page)
        img_list, next_page = parse_html(html)
        for img_link in img_list:
            down_pic(img_link)