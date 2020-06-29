# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:41:05 2020

@author: kcsof
"""

#Linear regression 

#If a student scored an 80 on the Math aptitude test, what grade would we expect them to achieve in Statistics? Determine the equation of the best-fit line using the least squares method, then compute and print the value of y when x=80 .

# x = [95,85,80,70,60]
# y = [85,95,70,65,70]

from statistics import mean, pstdev


def pearson(x, y):
    mx, sx, my, sy = mean(x), pstdev(x), mean(y), pstdev(y)
    return sum((xi - mx) * (yi - my) for xi, yi in zip(x, y)) / (len(x) * sx * sy)


def linear_regression(x, y):
    b = pearson(x, y) * pstdev(y) / pstdev(x)
    return mean(y) - b * mean(x), b


x, y = zip(*(map(float, input().split()) for _ in range(5)))
a, b = linear_regression(x, y)
print(f'{a+b*80:.3f}')