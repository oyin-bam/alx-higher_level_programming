#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_arg = len(sys.argv)
    sum = 0
    for i in range(1, num_arg):
        sum += int(sys.argv[i])
    print("{}".format(sum))
