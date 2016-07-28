#coding:utf-8

from bs4 import BeautifulSoup
import urllib2

of = open('proxy.txt','w')
get_proxyurl = 'http://www.kuaidaili.com/proxylist/'

for page in range(1,11):
	html = urllib2.urlopen(get_proxyurl+str(page)).read()
	soup = BeautifulSoup(html)
	trs = soup.find('table').find('tbody').find_all('tr')
	for tr in trs:
		tds = tr.find_all('td')
		ip = tds[0].text.strip()
		port = tds[1].text.strip()
		of.write('%s:%s\n' % (ip,port))
		print('%s:%s' % (ip,port))

of.close()