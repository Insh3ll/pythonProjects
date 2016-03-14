#coding=utf-8

import urllib
import re
import time

def getHtml(url):
    html=urllib.urlopen(url).read().decode('gb2312')
    return html

def getPicUrl(html):
    reg=r'lq/\d+'
    picUrlList=re.findall(reg,html)
    return picUrlList

def downloadPic(picUrlList):
    for picUrl in picUrlList:
        picName=picUrl[3:13]+'.jpg'
        picUrl='http://211.70.176.123/wap/'+picUrl+'.jpg'
        downloadPic=urllib.urlretrieve(picUrl,'D:\Desktop\getPic\pic\%s' % picName)
        time.sleep(1)
        print picUrl+'   OK!'
    return downloadPic
    
if __name__=='__main__':
    fxh=open('xh2.txt','r')
    for xh in fxh:
        xh=xh.strip()
        url='http://211.70.176.123/wap/zpjd.asp?xh='+xh
        
        html = getHtml(url)
        picUrlList = getPicUrl(html)
        downloadPic(picUrlList)
        
    fxh.close()
