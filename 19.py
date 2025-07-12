# Enter your code here. Read input from STDIN. Print output to STDOUT
x=input()
l=x.split()
x=int(l[0])
y=int(l[1])
l1=[]
l2=[]
for i in range(x):
    a=input()
    l1.append(a)
for i in range(y):
    a=input()
    l2.append(a)
for i in l2:
    if i not in l1:
        print("-1",end="")
    else:
        for j in range(len(l1)):
            if i==l1[j]:
                print(j+1,end=" ")
    print()


#problem link:
#https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true