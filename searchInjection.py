#coding:utf-8
import urllib
import urllib2
import re
import time
#from autoSqli import *

searchUrl = 'http://m.baidu.com/s?tn=middle&pn=pageNum&word=keyWord'
jumpUrl = 'http://m.baidu.com/?bdenc=1&nsrc='
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

def getUrlList(sUrl,jUrl):
	urlList = []
	#获取此sUrl中的10条nsrc记录
	html = getHtml(sUrl)
	nsrcList = regex_nsrc.findall(html)
	#遍历获取到的10条nsrc记录
	for nsrc in nsrcList:
		print ('.'),
		#测试（jUrl+nsrc）的可访问性
		#若跳转太多或访问出错
		#则跳过此条（jUrl+nsrc）
		html2 = getHtml(jUrl+nsrc)
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
		# 	u = urllib2.urlopen(jUrl+nsrc).geturl()
		# 	urlList.append(u)

	#返回获取到的真实url
	return urlList

def main():
	wd = 'inurl:php?id='
	wd = urllib.quote(wd)
	ksearchUrl = searchUrl.replace('keyWord',wd)
	for n in range(33,34):
		n = n * 10
		currentSearchUrl = ksearchUrl.replace('pageNum',str(n))
		print currentSearchUrl
		urlList = getUrlList(currentSearchUrl,jumpUrl)
		for url in urlList:
			print url
	f.close()
	return (0)

if __name__ == '__main__':
	start = time.time()
	f = open('sqliUrl.txt','a')
	main()
	print (time.time()-start)
