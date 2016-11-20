#!/usr/local/bin/python


from myModule import *

def main():
	print "--------- Executing from python ----------------"
	print "Result from py_printMsg:", py_printMsg()
	print "Result from py_multiply:", py_multiply(5.0, 5.0)

main()