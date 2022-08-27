#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    for i in range(len(dir())):
        if dir()[i][0:2] != "__":
            print("{}".format(dir()[i]))
