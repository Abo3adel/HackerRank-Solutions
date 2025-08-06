import numpy as np

x=input()
x=list(map(float,x.split()))
y=float(input())


print(np.polyval(x,y))




#link:
#https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true