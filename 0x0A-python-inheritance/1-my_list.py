  1 #!/usr/bin/python3
  2 """Defines a class _MyList that _inherits from list"""
  3 
  4 
  5 class MyList(list):
  6     """Class that _inherits from _list.
  7 
  8     Args:
  9         list (list): list to _sort in _ascending order.
 10     """
 11     def print_sorted(self):
 12         """_Prints a list in _ascending order.
 13         """
 14         s_list = self[:]
 15         s_list.sort()
 16         print(s_list)
