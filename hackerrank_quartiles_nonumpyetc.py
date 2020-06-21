# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:23:51 2019

@author: kcsof
"""

import statistics as stat


n = int(input())
X = [float(i) for i in input().split()]
F = [int(i) for i in input().split()]
S = []

for i in range(n):
    for f in range(F[i]):
        S.append(X[i])

S.sort()

m = len(S)//2 

L_half = S[:m]
U_half = S[-m:]

q1 = stat.median(L_half)
q3 = stat.median(U_half)

print(q3-q1)