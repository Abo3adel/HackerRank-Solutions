#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n%2==1:
    print("Weird")
elif n in [2,4]:
    print("Not Weird")
elif n in [6,8,10,12,14,16,18,20]:
    print("Weird")
elif n >20 and n%2==0:
    print("Not Weird")


#problem link:
#https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true