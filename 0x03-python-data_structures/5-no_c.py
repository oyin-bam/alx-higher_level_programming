#!/usr/bin/python3
def no_c(my_string):
    string_list = my_string.split()
    string_list.remove("cC")
    new_string = "".join(string_list)
    return new_string
