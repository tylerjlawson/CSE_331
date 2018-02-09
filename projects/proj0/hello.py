#!/usr/bin/python3
import getpass
import sys

with open('hello.txt', 'w') as writer:
	writer.write('hello, world\n')
	writer.write('I am {0}\n'.format(getpass.getuser()))
	writer.write('I am running Python {0}\n'.format(sys.version))

