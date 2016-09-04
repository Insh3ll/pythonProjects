# -*- coding: utf-8 -*-
# @Author: chen
# @Date:   2016-08-21 19:23:05
# @Last Modified by:   chen
# @Last Modified time: 2016-08-21 19:40:59

'''
092437
'''

def gener_man(of):
	for d in range(1,32):
		for i in range(100):
			for m in range(0,10,2):
				for j in range(10):
					t = '%02d%02d%d%d' % (d,i,m,j)
					print('Writing:%s' % t)
					of.write(t+'\n')


if __name__ == '__main__':
	of = open('womandic.txt','w')
	gener_man(of)
	of.close()