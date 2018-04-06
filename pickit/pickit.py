#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle


class PickIt(object):
    """
    Iterator for Pickle dumped file
    """
    def __init__(self, pickle_file_name, n=-1):
        self.fp = open(pickle_file_name, "rb")
        self.limit = n

    def __iter__(self, ):
        self.c = self.limit
        return self

    def __next__(self, ):
        ret = None
        if self.c == 0:
            raise StopIteration
        try:
            ret = pickle.load(self.fp)
        except:
            self.fp.close()
            raise StopIteration
        self.c -= 1
        return ret


if __name__ == '__main__':
    """
    Self Test
    """
    import sys

    filename = sys.argv[1]
    c = 0
    for _ in PickIt(filename):
        c += 1
    print(c)
