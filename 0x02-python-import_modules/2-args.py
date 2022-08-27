#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_of_arg = len(sys.argv)
    if num_of_arg == 1:
        print("{} arguments.".format(num_of_arg - 1))
    elif num_of_arg == 2:
        print("{} argument:".format(num_of_arg - 1))
    else:
        print("{} arguments:".format(num_of_arg - 1))

    for i in range(1, num_of_arg):
        print("{}: {}".format(i, sys.argv[i]))
