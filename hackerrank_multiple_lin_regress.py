# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:48:48 2020

@author: kcsof
"""

#Multiple Linear Regression
#for m+1 real constants (a, f1, f2,... , fm). We can say that the value of Y depends on m features. Andrea studies this equation for n different feature sets  and records each respective value of Y. If she has q new feature sets, can you help Andrea find the value of Y for each of the sets?

from sklearn import linear_model

def solve(y, x, x_pred):
  lm = linear_model.LinearRegression()
  lm.fit(x, y)
  y_pred = lm.predict(x_pred)
  return y_pred

def main():
  m, n = map(int, input().strip().split())
  y = []; x = []; x_pred = []
  for _ in range(n):
    *features, y_val = map(float, input().strip().split())
    x.append(features)
    y.append(y_val)

  for _ in range(int(input())):
    features = list(map(float, input().strip().split()))
    x_pred.append(features)
  
  answer = solve(y, x, x_pred)
  for num in answer:
    print(round(num, 2))

if __name__ == "__main__":
  main()