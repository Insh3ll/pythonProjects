#coding=utf-8

f=open('sfzh.txt','a')
a=raw_input(u'地区:  ')
y=raw_input(u'年:   ')
for m in xrange(12):
    m+=1
    m='%02d' %m
    m='%s' %m
    for d in xrange(31):
        d+=1
        d='%02d' % d
        d='%s' % d
        for b in xrange(10000):
            b='%04d' %b
            b='%s' % b
            sfzh=a+y+m+d+b
            f.write(sfzh+'\n')
                
f.close()
print 'done!'
