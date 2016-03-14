#coding=utf-8

import telnetlib

Host=raw_input("Host:")
user=raw_input("user:")
passwd=raw_input("passwd:")

    
tn=telnetlib.Telnet(Host)
tn.read_until('login:')
tn.write(user + '\n')
tn.read_until('password:')
tn.write(passwd + '\n')

tn.write(b"ls\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
