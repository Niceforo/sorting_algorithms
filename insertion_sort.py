#!C:\Python27
# -*- coding: utf-8 -*-
import sys, os, datetime

def insertion_sort1(a):

    for i in range(1, len(a)):

        j = i - 1
        elem = a[i]

        while j >= 0 and a[j] > elem:

            a[j + 1] = a[j]
            j = j - 1

        a[j + 1] = elem

    return a




a = [3, 15, 4, 1, 7, 9, 2, 23, 20]

print "insertion_sort1"
print a
print insertion_sort1(a), "\n"
