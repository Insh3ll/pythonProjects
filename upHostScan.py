#coding:utf-8
import nmap

def hostScan(tgthosts):
	nm = nmap.PortScanner()
	nm.scan(hosts=tgthosts,arguments='-n -sP -PE -PA21,23,80,3389')
	hosts_list = [(x,nm[x]['status']['state']) for x in nm.all_hosts()]
	for host,status in hosts_list:
		print (host+':'+status)

hostScan('172.16.1.0/24')