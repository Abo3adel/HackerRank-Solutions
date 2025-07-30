import numpy as np

x=input()
r=int(x[0])
c=int(x[2])
l1=[]
l2=[]
for i in range(r):
    x=input()
    l=list(map(int,x.split()))
    l1.append(l)
for i in range(r):
    x=input()
    l=list(map(int,x.split()))
    l2.append(l)            
            
a=np.array(l1)
b=np.array(l2)

print (a + b) 
print( a - b )   
print( a * b  )
print(a//b)
print( a % b  )
print( a ** b  )




#link:
#https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true