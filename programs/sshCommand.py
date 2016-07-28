#coding:utf-8
import pexpect
PROMPT = ['#','>>>','>','\$']
def sendCommand(child,cmd):
	child.sendline(cmd)
	child.expect(PROMPT)
	print (child.before)

def connect(host,user,passwd):
	ssh_newKey = "Are you sure want to continue connecting"
	connStr = 'ssh ' + user + '@' + host
	child = pexpect.spawn(connStr)
	rst = child.expect([pexpect.TIMEOUT,ssh_newKey,'[P|p]assword:'])
	if rst ==0 :
		print ('connecting error')
		return 
	if rst == 1 :
		child.sendline('yes')
		rst = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
		if rst == 0 :
			print ('connecting error')
			return
	child.sendline(passwd)
	child.expect(PROMPT)
	return child

def main():
	host = '127.0.0.1'
	user = 'Ins'
	passwd = '123456'
	child = connect(host,user,passwd)
	sendCommand(child,'cat /etc/passwd | grep root')

if __name__ == '__main__':
	main()