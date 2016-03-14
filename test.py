#coding:utf-8

fileurl=raw_input()

f=open(fileurl)

for line in f.readlines():
    print line

