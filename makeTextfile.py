'makeTextfile.py -- create text file'

import os
ls = os.linesep

while True:
	fname = raw_input("input a filename:")
	if os.path.exists(fname):
		print "ERROR: '%s' already exists" % fname
	else:
		break;

all = []
print "\nEnter lines ('.' by itself to quit).\n"

while True:
	entry = raw_input('> ')
	if entry == '.':
		break
	else:
		all.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print 'DONE!'