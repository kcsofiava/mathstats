# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 00:10:04 2020

@author: kcsof
"""
import statistics as stat
from math import sqrt


f = open("C:/Users/kcsof/input03.txt", "r")
f2 = (f.read())
f3 = ' '.join(f2.split()) 
numyes2 = [int(s) for s in f3.split() if s.isdigit()]

'''
listed = list(numyes2)
popped = listed.pop(0)

#n = int(input())
#X = [int(i) for i in input().split()]

def stddev(lst):
    mean = float(sum(lst)) / len(lst)
    return sqrt(sum((x - mean)**2 for x in lst) / len(lst))
    
def truncate(n, decimals=1):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


print(truncate(stddev(listed)))
'''
#it was key to use the population stdev
n,a=input(),list(map(int,input().split()))
print(round(pstdev(a),1))
