#!C:\Python27
# -*- coding: utf-8 -*-
import sys, os, datetime



def merge_sort1(a):

    if len(a) <= 1:
        return a

    left = a[ : len(a) / 2]
    right = a[len(a) / 2 : ]

    left = merge_sort1(left)
    right = merge_sort1(right)

    return merge(left, right)


def merge(left, right):

    RV = []

    while len(left) > 0 or len(right) > 0:

        if len(left) > 0 and len(right) > 0:

            if left[0] <= right[0]:
                RV.append(left[0])
                left = left[1:]

            else:
                RV.append(right[0])
                right = right[1:]

        elif len(left) > 0:
            RV.append(left[0])
            left = left[1:]

        elif len(right) > 0:
            RV.append(right[0])
            right = right[1:]

    return RV



l = [3, 4, 7, 15, 20, 21]
r = [1, 2, 5, 6, 19, 25, 30]

print "merge"
print l
print r
print merge(l, r), "\n"





a = [3, 15, 4, 1, 7, 9, 2, 23, 20]

print "merge_sort1"
print a
print merge_sort1(a), "\n"












