#coding:utf-8

s=raw_input('Input the code:')
print len(s)
r=input('Input the row:')
res=''

for i in range(r):
    res += s[i::r] 
print res
