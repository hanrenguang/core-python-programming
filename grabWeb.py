#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import urlretrieve

def firstNonBlank(lines):
	for eachLine in lines:
		if not eachLine.strip(): #如果该行是空格行
			continue
		else:
			return eachLine

def firstLast(webpage):
	f = open(webpage)
	lines = f.readlines()
	f.close()
	print firstNonBlank(lines),
	lines.reverse()
	print firstNonBlank(lines),

def download():
	url = raw_input('input the url you want to view: ')
	try:
		retval = urlretrieve(url)[0] #urlretrieve()直接将数据下载到本地
	except IOError:
		retval = None
	if retval:
		firstLast(retval)

if __name__ == '__main__':
	download()