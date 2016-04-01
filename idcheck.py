#!usr/bin/env python
# -*- coding: utf-8 -*-
'检查标识符是否合法'

import string

alphas = string.letters + "_"
nums = string.digits

print "welcome to the identifier Checker v1.0"
print "Testes must be at least 2 chars long."
myInput = raw_input("Identifier to test?")

flag = 1

if len(myInput) > 1:
	if myInput[0] not in alphas:
		print "invalid: first symbol must be alphabetic"
	else:
		for otherChar in myInput[1:]:
			if otherChar not in alphas + nums:
				print "invalid: remaining symbols must be alphanumeric"
				break
			else:
				flag += 1

	if (flag == len(myInput)):
		print myInput + "is a reasonable id."
else:
	print "okay as an identifier"