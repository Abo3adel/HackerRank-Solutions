# Enter your code here. Read input from STDIN. Print output to STDOUT
x=int(input())
l={}
names=[]
for i in range(x):
    r=input()
    names.append(r)
    l[r]=0
    
for i in names:
    l[i]+=1
    
print(len(l))

for i in names:
    if l[i]>0:
        print(l[i],end=' ')
        l[i]=0
        


#problem link:
#https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true