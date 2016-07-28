#coding:utf-8
import nmap
import optparse

def portScan(tgtHost,tgtPort):
	nmScan = nmap.PortScanner()
	results = nmScan.scan(tgtHost,tgtPort)
	state = results['scan'][tgtHost]['tcp'][int(tgtPort)]['state']
	portName = results['scan'][tgtHost]['tcp'][int(tgtPort)]['name']
	print ('[*]Tcp:'+tgtHost+'/'+tgtPort+'('+portName+')'+':'+state)

def hostScan(tgthosts):
	nm = nmap.PortScanner()
	nm.scan(hosts=tgthosts,arguments='-n -sP -PE -PA21')
	hosts_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]
	for host,state in hosts_list:
		if state == 'up':
			print (host+':'+state)
			return True
	return False

def main():
	parser = optparse.OptionParser('usage %prog -H <targetIP> -p <targetPort>')
	parser.add_option('-H',dest='tgtIP',help='specify target Host')
	parser.add_option('-p',dest='tgtPorts',help='specify target Ports')
	(options,args) = parser.parse_args()
	tgtIP = options.tgtIP
	tgtPorts = options.tgtPorts
	if (tgtIP == None) or (tgtPorts == None):
		print (parser.usage)
		exit(0)
	tgtPorts = tgtPorts.split(',')
	if (hostScan(tgtIP)):
		for tgtPort in tgtPorts:
			portScan(tgtIP,tgtPort)

if __name__ == '__main__':
	main()
