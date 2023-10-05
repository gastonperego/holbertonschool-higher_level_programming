#!/usr/bin/python3
"""A"""


class MyList(list):
    """" d """

    def print_sorted(self):
        """" d """

        if all(isinstance(i, int) for i in self):
            print(sorted(self))
        else:
            raise TypeError("All elements must be integers")
