# Enter your code here. Read input from STDIN. Print output to S
import numpy as np
x=int(input())

l=[]

for i in range(x):
    ll=list(map(float,input().split()))
    l.append(ll)
    
a=np.array(l)

print(round(np.linalg.det(a),2))

#link:
#https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true