#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    n_list = []
    for i in range(0, list_length):
        try:
            n_list.append((my_list_1[i]) / (my_list_2[i]))
        except (ZeroDivisionError):
            n_list.append(0)
            print("division by 0")
        except (TypeError):
            n_list.append(0)
            print("wrong type")
        except (IndexError):
            n_list.append(0)
            print("out of range")
        finally:
            continue

    return n_list
