#coding:utf-8
import re
import urllib2

url = 'http://m.baidu.com/s?tn=middle&pn=300&word=inurl%3Aphp%3Fid%3D'
url2 = 'http://m.baidu.com/?bdenc=1&nsrc='
regex_nsrc = re.compile(r'nsrc=(.*?)"')
regex_url = re.compile(r'url=(http://.*)"')
def getHtml(url):
	try:
		page = urllib2.urlopen(url)
		html = page.read()
		return html
	except Exception, e:
		pass
	return 'Error'

def getUrlList():
	html = getHtml(url)
	nsrcList = regex_nsrc.findall(html)
	urlList = []
	p = 0
	for nsrc in nsrcList:
		p += 1
		print ('Tring page:%d' % p)
		#测试（url2+nsrc）的可访问性
		#若跳转太多或访问出错
		#则跳过此条（url2+nsrc）
		html2 = getHtml(url2+nsrc)
		if html2 == 'Error':
			print html2
			continue
		#成功获取到跳到百度转码的网页（html2）
		u = regex_url.search(html2)
		if u:
			urlList.append(u.group(1).replace('amp;',''))
		#直接跳转到真实网页,由于不同的网站的
		#网络环境不同会导致访问时间可能太长，故屏蔽
		# else:
		# 	u = urllib2.urlopen(url2+nsrc).geturl()
		# 	urlList.append(u)
	return urlList

for url in getUrlList():
	print url