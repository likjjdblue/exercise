#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def ZipNonInterator(*args):
    TmpMinLen = float('inf')
    for _ in range(len(args)):
        TmpMinLen = min (TmpMinLen, len(args[_]))

    TmpResult = list()
    for round in range(TmpMinLen):
        TmpCurrentList = list()
        for index in range(len(args)):
            TmpCurrentList.append(args[index][round])
        TmpResult.append(tuple(TmpCurrentList))

    print (TmpResult)
    return TmpResult


if __name__ == '__main__':
    TmpListA = [1, 2, 3]
    TmpListB = [4, 5, 6]
    TmpListC = [7, 8, 9]

    pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]


    ZipNonInterator(TmpListA, TmpListB, TmpListC)
    ZipNonInterator(*pairs)