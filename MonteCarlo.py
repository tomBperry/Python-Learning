from random import *
import decimal

n = 10000000
d = 2
r = 1

count = 0
tempSum = 0

for i in range(n):
    for j in range(d):
        x = decimal.Decimal(2 * r * (random() - 0.5))
        tempSum += x ** 2
    if tempSum <= r ** 2:
        count += 1
    tempSum = 0

ratio = decimal.Decimal(count / n)
pi = ratio * 4
print(pi)