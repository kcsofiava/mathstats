# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:19:03 2020

@author: kcsof
"""

#Geometric Distributions

#The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the 5th inspection?


def geometric_distributon(n, p):
    return ((1-p)**(n-1))*p

a, b = list(map(int, input().split()))
n = int(input())
print('{:.3f}'.format(geometric_distributon(n, a/b)))

#The probability that a machine produces a defective product is 1/3 . What is the probability that the 1st defect is found during the first 5 inspections?

def geo_dist2(n, p):
    return (1-p)**(n-1) * p

num, denom = map(int, input().split())
p = num/denom
n = int(input())
print(round(sum([geo_dist2(i, p) for i in range(1,n+1)]),3))