#coding=utf8

start_num='13120602'

fxh=open('xh2.txt','w')
for i in xrange(100):
    i='%02d' % i
    i='%s' % i
    xh = start_num+i+'\n'
    fxh.write(xh)
fxh.close()
print 'ok!'
