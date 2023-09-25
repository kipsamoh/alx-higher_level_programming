#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
	to_print = 0

	for i in range (x):
		try:
		print("{}".format(my_list[i], end=''))
		except:
		    break:
		else:
		to_print = to_print + 1

		print()
	return(to_print)
