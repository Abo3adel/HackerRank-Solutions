# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input()
l=[]
l1=[]
l2=[]
l3=[]
for i in x:
    if i.isupper():
        l.append(i)
    elif i.islower():
        l1.append(i)
    elif (ord(i)-ord('0'))%2==0:
        l2.append(i)
    else:
        l3.append(i)
l.sort()
l1.sort()
l2.sort()
l3.sort()
x="".join(l)
y="".join(l1)
z="".join(l2)
aha="".join(l3)
print(y+x+aha+z)



#problem link:
#https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true