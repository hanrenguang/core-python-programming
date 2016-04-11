#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import urllib2
import re

filename = "e:\\python\\crawl.txt"
fp = open(filename,"w")

url = "http://www.qiushibaike.com"
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"
headers = {"User-Agent" : user_agent}

try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode("utf-8")
	pattern = re.compile('<div.*?content">(.*?)<!--.*?-->.*?</div>',re.S)
	items = re.findall(pattern,content)
	item = items[0].encode('utf-8')
	fp.write(item)
	fp.close()
except urllib2.URLError, e:
	if hasattr(e,"code"):
		print e.code
	if hasattr(e,"reason"):
		print e.reason