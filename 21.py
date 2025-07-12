# Enter your code here. Read input from STDIN. Print output to STDOUT
t=int(input())
for i in range(t):
    x=int(input())
    lai=[]
    s=input()
    lai= s.split()
    li=[int(i) for i in lai]
    #print(li)
    l=0
    r=len(li)-1
    temp=100000000000000
    f=False
    while l<r:
        if li[l]>li[r]:
            if li[l]<=temp:
                temp=li[l]
                l+=1
            else:
               f=True
               break 
        elif li[l]<li[r]:
            if li[r]<=temp:
                temp=li[r]
                r-=1
            else:
               f=True
               break             
        else:
            if li[l]<=temp:
                temp=li[l]
                l+=1
                r-=1
            else:
               f=True
               break 
    if f :
        print("No")
    else:
        print("Yes")
    
                 
            
            
            
            
            
            
            
            
#problem link:
#https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true           
            
