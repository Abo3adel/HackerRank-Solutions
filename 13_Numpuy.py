# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
x=input()
x=list(map(int,x.split()))
y=input()
y=list(map(int,y.split()))

a=np.array(x)
b=np.array(y)


print(np.inner(a,b))
print(np.outer(a,b))



#link:
#https://www.hackerrank.com/challenges/np-inner-and-outer/problem?isFullScreen=true