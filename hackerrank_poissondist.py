# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 16:04:57 2020

@author: kcsof
"""
#Hackerrank Poisson Distribution

#A random variable, X follows Poisson distribution with mean of 2.5 . Find the probability with which the random variable X is equal to 5 .
from math import factorial, exp

mu = float(input())
x = int(input())
poissonprob = ((mu ** x) * exp(-mu)) / factorial(x)
print("%.3f" %poissonprob)


#The manager of a plant is planning to buy a machine either type A or B. For each day's operation:
# Number of repairs X that machine A needs is Poisson var with mean 0.88. Daily cost of operating A is Ca = 160 + 40X^2
# Number of repairs Y that machine B needs is Poisson var with mean 1.55. Daily cost of operating B is Cb = 128 + 40Y^2
# Assume that the repairs take a negligible amount of time and the machines are maintained nightly to ensure that they operate like new at the start of each day. Find and print the expected daily cost for each machine.


# Input from stdin
averageX, averageY = [float(num) for num in input().split(" ")]

# Cost
CostX = 160 + 40*(averageX + averageX**2)
CostY = 128 + 40*(averageY + averageY**2)

print(round(CostX, 3))
print(round(CostY, 3))