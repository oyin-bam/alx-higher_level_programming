#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    check_list = my_list.copy()
    if idx < 0:
        return check_list
    elif idx > (len(my_list) - 1):
        return check_list
    else:
        check_list[idx] = element
        return checklist_list
