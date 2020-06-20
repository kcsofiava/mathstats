# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:23:51 2019

@author: kcsof
"""

import statistics as stat


n=int(input())
arr=sorted(map(int,input().split()))

print(int(stat.median(arr[:n//2])))
print(int(stat.median(arr)))
print(int(stat.median(arr[(n+1)//2:])))