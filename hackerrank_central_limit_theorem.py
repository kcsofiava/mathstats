# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:00:40 2020

@author: kcsof
"""

#Central Limit Theorem

#A large elevator can transport a maximum of 9800 pounds. Suppose a load of cargo containing 49 boxes must be transported via the elevator. The box weight of this type of cargo follows a distribution with a mean of 205 pounds and a standard deviation of 15 pounds. Based on this information, what is the probability that all 49 boxes can be safely loaded into the freight elevator and transported?

import math

x = int(input())
n = int(input())
mu = int(input())
sigma = int(input())

mu_sum = n * mu 
sigma_sum = math.sqrt(n) * sigma

def cdf(x, mu, sigma):
    Z = (x - mu)/sigma
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(cdf(x, mu_sum, sigma_sum), 4))

#The number of tickets purchased by each student for the University X vs. University Y football game follows a distribution that has a mean of 2.4 and a standard deviation of 2.0.

#A few hours before the game starts, 100 eager students line up to purchase last-minute tickets. If there are only 250 tickets left, what is the probability that all 100 students will be able to purchase tickets?

import math
x = 250
n = 100
sampling_mean = 2.4
sampling_stdev = 2.0
stdev = sampling_stdev * math.sqrt(n)

cdf = 0.5 * (1 + math.erf((x - sampling_mean * n) / (stdev * math.sqrt(2))))

print(round(cdf,4))

#You have a sample of 100 values from a population with mean 500  and with standard deviation 80 . Compute the interval that covers the middle 95% of the distribution of the sample mean; in other words, compute A and B such that P(A < x < B) =0.95 . Use the value of z=1.96 . Note that z is the z-score.

samples = float(input())
mean = float(input())
sd = float(input())
interval = float(input())
z = float (input())

sd_sample = sd / (samples**0.5)
print(round(mean - sd_sample*z,2))
print(round(mean + sd_sample*z,2))
