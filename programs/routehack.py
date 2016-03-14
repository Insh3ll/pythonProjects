# -*- coding: utf-8 -*-

import urllib
import httplib
import threading

headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		"Accept-Encoding": "gzip, deflate",
		"Referer": "http://192.168.1.1/rpAuth.html",
		"Connection": "keep-alive",
		"Content-Type": "application/x-www-form-urlencoded"};

lock=threading.Lock()

def TryPasswd():
	global headers
	conn=httplib.HTTPConnection("192.168.1.1")
	i=1
	LoginPassword='ZyXEL+ZyWALL+Series'
	Prestige_Login='%B5%C7%C2%BC'
	while i>0:
		line=inFile.readline()
		passwd=line.strip('\n')
		username='admin'
		params=urllib.urlencode({'LoginUsername':username,
					 'hiddenPassword':passwd,
					 'LoginPassword':LoginPassword,
					 'Prestige_Login':Prestige_Login,
					 'LockUserFlag':0})
		conn.request(method="POST", url="/rpAuth.html", body=params, headers=headers)
		responseText = conn.getresponse().read()
		outFile = open('route.html', 'w')
		outFile.write(responseText)
		outFile.close()
		print params
		#print responseText
		i=i-1
		
		
with open(r'passwd.txt', 'r') as inFile:
    TryPasswd()
		
