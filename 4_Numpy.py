import numpy as np
ll=[]
x= input()
a,b,c=list(map(int,x.split()))
for i in range(a+b):
    x=input()
    l=list(map(int,x.split()))
    ll.append(l)
    
print(np.array(ll))


#link:
#https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true