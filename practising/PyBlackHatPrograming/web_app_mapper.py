# -*- coding: utf-8 -*-
# @Author: chen
# @Date:   2016-09-04 21:25:33
# @Last Modified by:   root
# @Last Modified time: 2016-09-05 09:30:41

import urllib2
import threading
import Queue
import urllib
import requests

threads = 10
tgt_url = 'http://testphp.vulnweb.com'

wordlist_file = '/tmp/small.txt'
resume = None
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'

def build_wordlist(fp):
	fd = open(wordlist_file,'rb')
	raw_words = fd.readlines()
	fd.close()

	found_resume = False

	words = Queue.Queue()

	for word in raw_words:
		word  = word.strip()
		if resume is not None:
			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = True
					print ('Resuming wordlist from: %s ' % resume)
		else:
			words.put(word)

	return words

def dir_burp(word_queue,extensions=None):
	while not word_queue.empty():
		attempt = word_queue.get()
		attempt_list = []
		if '.' not in attempt:
			attempt_list.append('/%s/' % attempt)
		else:
			attempt_list.append('/%s' % attempt)

		if extensions:
			for extension in extensions:
				attempt_list.append('/%s%s' % (attempt,extension))

		for burp in attempt_list:
			url = '%s%s' % (tgt_url,urllib.quote(burp))
			print('Testing: %s ' % url)

			try:
				headers = {}
				headers['User-Agent'] = user_agent

				rsp = requests.get(url,headers=headers)
				if len(rsp.read()):
					print('[%d]=> %s' % (rsp.code,url))
			except urllib2.URLError,e:
				if hasattr(e,'code') and e.code != 404:
					print('!!! %d => %s' % (e.code,url))

def main():
	extensions = ['.php','.bak','.inc','rar']
	word_queue = build_wordlist(wordlist_file)
	for i in range(threads):
		t = threading.Thread(target=dir_burp,args=(word_queue,))
		t.start()

if __name__ == '__main__':
	main()