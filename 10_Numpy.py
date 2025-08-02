# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np


x,y=list(map(int,input().split()))
l=[]
for i in range(x):
    ll=list(map(int,input().split()))
    l.append(ll)
    
li=np.array(l)
print(np.max(np.min(li,axis=1)))


#link:
#https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true