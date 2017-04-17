#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

class PickIt(object):
    def __init__(self, pickle_file_name, n = -1):
        self.fp = open(pickle_file_name, "rb")
        self.loadmax = n

    def __iter__(self, ):
        self.idx = self.loadmax
        return self

    def __next__(self, ):
        ret = None
        if self.idx != 0:
            try:
                ret = pickle.load(self.fp)
                self.idx -= 1
            except:
                self.fp.close()
        else:
            raise StopIteration
        return ret

    def __del__(self, ):
        self.fp.close()
