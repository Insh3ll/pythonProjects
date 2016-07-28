#!/usr/bin/python
#coding:utf-8
from multiprocessing import Process, Queue

q = Queue()

def consumer_worker(q):
    for item in iter(q.get, 'STOP'):
        print item

def producer_worker(q):
    for i in xrange(1,100):
        q.put("Hello World!!!")
    q.put('STOP')
    
p = Process(target=producer_worker, args=(q,))
p.start()
p.join()

p1 = Process(target=consumer_worker, args=(q,))
p1.start()
p1.join()

exit()