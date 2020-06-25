# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:48:43 2020

@author: kcsof
"""

#binomial distribution: the ratio of boys to girls for babies born in Russia is 1.09 : 1. If there is 1 child born per birth, what proportion of Russian families with exactly 6 chilcdren will have at least 3 boys?

import math

def binomial_dist(x, n, p):
    b = (math.factorial(n)/(math.factorial(x)*math.factorial(n-x)))*(p**x)*((1-p)**(n-x))
    return(b)

b, p, n = 0, 1.09/2.09, 6
for i in range(3,7):
    b += binomial_dist(i, n, p)   
print("%.3f" %b)


'''

#A manufacturer of metal pistons finds that, on average, 12%  of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of  pistons will contain:
#No more than 2 rejects?
#At least 2 rejects?

from math import factorial

r, p = map(float, input().split())

def comb(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

print(round(sum([comb(p, i) * (r / 100)**i * ((100 - r) / 100)**(p - i)  for i in range(0, 3)]), 3))
print(round(sum([comb(p, i) * (r / 100)**i * ((100 - r) / 100)**(p - i)  for i in range(2, 11)]), 3))
'''