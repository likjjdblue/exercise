#!/usr/bin/env python2
'''
Tony Hoare’s Quicksort tutorial
'''
import random

def quickSort(tmpList):
    if len(tmpList) < 2:
        return tmpList

    tmpMiddleIndex = int(len(tmpList) / 2)
    tmpMiddleValue = tmpList[tmpMiddleIndex]
    tmpLessThanList = list(filter(lambda x:x <tmpMiddleValue, tmpList))
    tmpGreatThanList = list(filter(lambda x:x >tmpMiddleValue, tmpList))

    tmpLessThanList = quickSort(tmpLessThanList)
    tmpGreatThanList = quickSort(tmpGreatThanList)
    return tmpLessThanList + [tmpMiddleValue] + tmpGreatThanList



tmpList = [x for x in range (19)]
random.shuffle(tmpList)

print (quickSort(tmpList))