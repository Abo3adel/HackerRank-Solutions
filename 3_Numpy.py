# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

inp = input()
ll=[]
#a,b=list(map(int,inp.split()))
a=int(inp[0])
b=int(inp[2])
for i in range(a):
    x=input()
    l=list(map(int,x.split()))
    ll.append(l)

lll=np.array(ll)
print (np.transpose(lll))
print(lll.flatten())


#link:
#https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true