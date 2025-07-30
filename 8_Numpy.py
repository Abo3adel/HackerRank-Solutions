import numpy as np

np.set_printoptions(legacy="1.13")

x=input()
l=np.array(list(map(float,x.split())))

print(np.floor(l))
print(np.ceil(l))            
print(np.rint(l))  

#link:
#https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true