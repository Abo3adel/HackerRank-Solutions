# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy  as np
x= int(input())

l=[]
for i in range(x):
    ll=list(map(int,input().split()))
    l.append(ll)
    
l1=[]
for i in range(x):
    ll=list(map(int,input().split()))
    l1.append(ll)
a=np.array(l)
b=np.array(l1)

print(np.dot(a,b))








#link:
#https://www.hackerrank.com/challenges/np-dot-and-cross/problem?isFullScreen=true