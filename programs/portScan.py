#coding:utf-8
import optparse
import socket
import threading

screenlock = threading.Semaphore(value=1)
def connScan(tgtIP,tgtport):
	try:
		connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		connSkt.connect((tgtIP,tgtport))
		connSkt.send('Ins\r\n')
		results = connSkt.recv(100)
		screenlock.acquire()
		print ('[+]%d/tcp open' % tgtport)
		print ('[+]' + str(results))
	except Exception, e:
		screenlock.acquire()
		print ('[-]%d/tcp close' % tgtport)
		#raise e
	finally:
		screenlock.release()
		connSkt.close()

def portScan(tgthost,tgtports):
	try:
		tgtIP = socket.gethostbyname(tgthost)
	except Exception, e:
		print ('[-]Cannot resolve "%s" : unkonw host' % tgthost)
		return 
	try:
		tgtName = socket.gethostbyaddr(tgtIP)
		print ('\n[+]Scan result for:'+ tgtName[0])
	except Exception, e:
		print ('\n[+]Scan Result for:' + tgtIP)
	socket.setdefaulttimeout(10)
	tgtports = tgtports.split(',')
	for tgtport in tgtports:
		#print ('Scaning Port:' + tgtport)
		t = threading.Thread(target=connScan,args=(tgtIP,int(tgtport)))
		t.start()

def main():
	parser = optparse.OptionParser('usage %prog -H <targethost> -p <targetport>')
	parser.add_option('-H',dest='tgthost',type='string',help='specify target host')
	parser.add_option('-p',dest='tgtports',type='string',help='secify target port')
	(options,args) = parser.parse_args()
	tgthost = options.tgthost
	tgtports = options.tgtports
	if (tgthost == None) or (tgtports == None):
		print (parser.usage)
		exit(0)
	portScan(tgthost,tgtports)

if __name__ == '__main__':
	main()















