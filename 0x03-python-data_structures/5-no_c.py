#!/usr/bin/python3
def no_c(my_string):
    # specifying the mapping using ASCII
    table = {ord('c'): None, ord('C'): None}
    new_string = my_string.translate(table)
    return new_string
