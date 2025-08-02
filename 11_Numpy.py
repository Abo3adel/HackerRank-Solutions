# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np


x,y=list(map(int,input().split()))
l=[]
for i in range(x):
    ll=list(map(int,input().split()))
    l.append(ll)
li=np.array(l)
print(np.mean(li, axis=1))
print(np.var(li, axis=0))
print(round(np.std(li), 11))

#link:
#https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true