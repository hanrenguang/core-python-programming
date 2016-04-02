#!/usr/bin/env python
# -*- coding: utf-8 -*-

'用于管理用户名和密码的模拟登录数据系统'

db = {}

def newuser():
	prompt = 'login desired: '
	while True:
		name = raw_input(prompt)
		if db.has_key(name):
			prompt = 'name token, try another: '
			continue
		else:
			break
	pwd = raw_input('password: ')
	db[name] = pwd

def olduser():
	name = raw_input('login: ')
	pwd = raw_input('password: ')
	passwd = db.get(name)
	if passwd == pwd:
		print 'welcome back',name
	else:
		print 'login incorrect'

def showmenu():
	prompt = '''
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice: '''
	lb = {'n':newuser, 'e':olduser}
	while True:
		while True:
			try:
				choice = raw_input(prompt).strip()[0].lower()
			except (EOFError, KeyboardInterrupt):
				choice = 'q'
			print '\nYou picked: [%s]' % choice
			if choice not in 'neq':
				print 'invalid option, try again'
			else:
				break
		if choice == 'q':
			break
		lb[choice]()

if __name__ == '__main__':
	showmenu()