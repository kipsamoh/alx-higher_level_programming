#!/usr/bin/python3
def safe_print_integer_err(value):
	import sys
	try:
	    print("{:d}".format(value))
	except exception as e:
	    sys.stderr.write("exception: {}\n".format,(e))
	    return false
	else
	    return true
