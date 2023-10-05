#!/usr/bin/python3
""" s """


def inherits_from(obj, a_class):
    """ a """

    return True if issubclass(type(obj), a_class)  and a_class != type(obj) else False