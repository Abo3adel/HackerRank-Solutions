# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np


x,y=list(map(int,input().split()))
l=[]
for i in range(x):
    ll=list(map(int,input().split()))
    l.append(ll)
    
    
arr= np.array(l)
l=np.sum(arr,axis=0)
mul=1
for i in l:
    mul*=i
    
print(mul)



#link:
#https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true