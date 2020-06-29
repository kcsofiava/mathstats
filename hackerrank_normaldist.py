# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 13:33:14 2020

@author: kcsof
"""

#Hackerrank Normal Distributions

#In a certain plant, the time taken to assemble a car is a random variable,X, having a normal distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability that a car can be assembled at this plant in:

#Less than 19.5 hours?
#Between 20 and 22 hours?

import math


mu, std = list(map(int, input().rstrip().split()))
h1_1 = float(input())
h2_1, h2_2 = list(map(float, input().rstrip().split()))

def normed_cdf(x):
    erf_parameter = (x - mu) / (std * math.sqrt(2))
    return 0.5 * (1 + math.erf(erf_parameter))

result_1 = normed_cdf(h1_1)
print(round(result_1, 3))
result_2 = normed_cdf(h2_2) - normed_cdf(h2_1)
print(round(result_2, 3))


'''
import math
mean, std = 20, 2
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))

# Less than 19.5
print('{:.3f}'.format(cdf(19.5)))
# Between 20 and 22
print('{:.3f}'.format(cdf(22) - cdf(20)))
'''

# for a population of students,final grades for an exam has mu is 70
#sigma is 10
#what percentage scored grade > 80
# "" scored >= 60
# "" scored < 60

import math
mean, std = 70, 10
cdf = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round((1-cdf(80))*100,2))
print(round((1-cdf(60))*100,2))
print(round((cdf(60))*100,2))