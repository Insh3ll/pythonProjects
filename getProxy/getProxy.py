#coding:utf-8

from bs4 import BeautifulSoup
import requests


def get_proxies(url,of):
	for page in range(1,3) :
		html = requests.get(url+str(page)).text
		soup = BeautifulSoup(html)
		trs = soup.find('table').find('tbody').find_all('tr')
		for tr in trs:
			tds = tr.find_all('td')
			ip = tds[0].text.strip()
			port = tds[1].text.strip()
			protocol = tds[3].text.strip()
			of.write('%s://%s:%s\n' % (protocol,ip,port))
			print('{0}://{1}:{2}'.format(protocol,ip,port).split(', ')[-1])


def check_proxies(f):
	headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
	while True:
		line = f.readline()
		if not line:
			break
		proxy = line.strip().split('//')[1]
		proxies = {'http':'http://'+proxy}
		print(proxies)
		try:
			r = requests.get('http://www.kuaidaili.com/',proxies=proxies,timeout=3)
			print(r.status_code)
		except:
			pass

if __name__ == '__main__':
	get_proxyurl = 'http://www.kuaidaili.com/proxylist/'
	with open('proxies.txt','w') as f:
		get_proxies(get_proxyurl,f)
	with open('proxies.txt','r') as f:
		check_proxies(f)
	
