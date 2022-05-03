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



TmpListA = [1, 2, 3]
TmpListB = [4, 5, 6]
TmpListC = [7, 8, 9]

ZipNonInterator(TmpListA, TmpListB, TmpListC)