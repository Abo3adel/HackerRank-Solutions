# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np

user_input=input()
numbers = list(map(int, user_input.split()))
a= np.array(numbers)
a.shape=(3,3)
print(a)

#link:
#https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true