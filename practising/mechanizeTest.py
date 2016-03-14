#coding:utf-8
import mechanize

def testProxy(url,proxy):
	browser = mechanize.Browser()
	browser.set_proxies(proxy)
	page = browser.open(url)
	html = page.read()
	print html

url = 'http://ip138.com/'
hideMeProxy = {'http':'117.164.132.237:8123'}
testProxy(url,hideMeProxy)