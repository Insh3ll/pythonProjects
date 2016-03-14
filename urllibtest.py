#coding=utf-8

import urllib

url='http://'+raw_input('input the url:http://')
html=urllib.urlopen(url).read()
print html