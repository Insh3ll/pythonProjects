# -*- coding:utf-8 -*-

import threading
import time
import os

def music(k):
    for i in range(2):
        print('I was listing to %s : %s '% (k,time.ctime()))
        time.sleep(1)

def movie(k):
    for i in range(2):
        print('I was watching %s : %s '% (k,time.ctime()))
        time.sleep(5)
ths=[]
t1 = threading.Thread(target=music,args=(u'小幸运',))
t2 = threading.Thread(target=movie,args=(u'阿凡达',))
ths.append(t1)
ths.append(t2)

if __name__ == '__main__':
    for t in ths:
        t.start()
    for t in ths:
        t.join()
    print('all over %s' % time.ctime())