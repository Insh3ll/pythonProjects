# -*- coding: utf-8 -*-
# @Author: chen
# @Date:   2016-08-24 13:28:54
# @Last Modified by:   chen
# @Last Modified time: 2016-08-24 17:36:09

import time
from bs4 import BeautifulSoup
import requests
import codecs

loginurl = 'http://yingxin.hfuu.edu.cn/userPasswordValidate.portal'
xxcjurl = 'http://yingxin.hfuu.edu.cn/index.portal?.pn=p65498'

def dologin(xh,pw):
	s = requests.session()
	data = {'Login.Token1':xh,'Login.Token2':pw}
	resp = s.post(loginurl,data=data).text
	assert 'LoginSuccessed' in resp
	#print(resp)
	return s

def xxcj_parser(s,of):
	xxcj_html = s.get(xxcjurl).text
	xxcj_bs = BeautifulSoup(xxcj_html,'html.parser')
	#welcomeMsg = xxcj_bs.find(id='welcomeMsg').getText()
	tables = xxcj_bs.find_all('table',attrs={'class':'w-main-table'})
	xh = tables[0].find_all('tr')[2].find_all('td')[1].getText().strip()
	xm = tables[0].find_all('tr')[2].find_all('td')[2].getText().strip()
	ssl = tables[0].find_all('tr')[6].find_all('td')[0].getText().strip()
	fjh = tables[0].find_all('tr')[6].find_all('td')[1].getText().strip()
	ch = tables[0].find_all('tr')[6].find_all('td')[2].getText().strip()
	phone = tables[1].find_all('tr')[1].find_all('td')[0].getText().strip()
	qq = tables[1].find_all('tr')[3].find_all('td')[0].getText().strip()
	reach_time = tables[2].find_all('tr')[1].find_all('td')[1].getText().strip()
	print('| %s | %s | %s | %s | %s | %s | %s | %s |' % (xh,xm,ssl,fjh,ch,phone,qq,reach_time))
	of.write('| %s | %s | %s | %s | %s | %s | %s | %s |\n' % (xh,xm,ssl,fjh,ch,phone,qq,reach_time))
	of.write('---------------------------------------------------------------------------------------\n')

def main():	
	f = open('xh_pw.txt','r')
	of = codecs.open('yingxininfo.txt','a','utf-8') 
	while  True:
		line = f.readline().strip()
		if line == '':
			break
		xh = line.split('----')[0]
		pw = line.split('----')[1]
		print(xh,pw)
		s = dologin(xh,pw)
		#xxcj_parser(s,of)
	of.close()
	f.close()

if __name__ == '__main__':
	main()