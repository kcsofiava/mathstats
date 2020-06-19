# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:02:34 2020

@author: kcsof
"""

def weighted_mean(numbers, weights):
    total = sum([num*weight for num,weight in zip(numbers,weights)])
    print(round(total / sum(weights),1))

numbers = int(input()) # Not needed; so overwrite var with next input
numbers = map(float, input().split())
weights = list(map(int, input().split()))

weighted_mean(numbers, weights)