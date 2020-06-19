# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:16:24 2020

@author: kcsof
"""
#Mean, Median, Mode

import sys 
import numpy as np


my_input = sys.stdin.read()

f = open("input04.txt", "r")
f2 = (f.read())
f3 = ' '.join(f2.split()) 
numyes2 = [int(s) for s in f3.split() if s.isdigit()]


listed = list(numyes2)
popped = listed.pop(0)


mean = np.mean(listed)
median = np.median(listed)
#mode = stats.mode(numyes)
mode = max(sorted(listed), key=listed.count)

print(mean)
print(median)
print(mode)