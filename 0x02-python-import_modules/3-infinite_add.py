#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total_args = 0
    for arg in sys.argv:
        if arg != sys.argv[0]:
            total_args += int(arg)
    print(total_args)
