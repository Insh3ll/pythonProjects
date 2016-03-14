#coding:utf-8
import urllib
import urllib2
import cookielib
import re

#第一次build_opener的时候，把对应的cookiejar传进去  
#以后每次的http的request，都会自动包含了cookie，而不需要我们操心了
cj = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

url = 'http://ctf.idf.cn/game/pro/37/' #请求的页面
req = urllib2.Request(url)

res = urllib2.urlopen(req)
html = res.read()

s = re.findall('<hr \/>\s*(.*)\s*<hr \/>',html)  #匹配满足条件的数据

#循环处理匹配到的每个字符
s = s[0]
w = 0
o = 0
l = 0
d = 0
y = 0
for i in s:
	if i == 'w':
		w += 1
	if i == 'o':
		o += 1
	if i == 'l':
		l += 1
	if i == 'd':
		d += 1
	if i == 'y':
		y += 1
count = str(w)+str(o)+str(l)+str(d)+str(y)
		
data = {'anwser':count}
data = urllib.urlencode(data)
res = urllib2.urlopen(url,data)

print res.read()