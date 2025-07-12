def print_rangoli(size):
    il=96
    n=size
    #print(chr(i+n))
    #end='-'
    x=(n-1)*2
    y=0
    for i in range(n):
        for j in range(x):
            print('-',end="")
        for j in range(0,y+1 ):
            if j!=y:
               print(chr(il+n-j),end="-")
            else:
              print(chr(il+n-j),end="")  
        for j in range(n-y,n):
            print("-",chr(il+j+1),end="",sep="")
        for j in range(x):
            print('-',end="")
        x-=2
        y+=1
        print()
    x=x*-1
    y-=2
    for i in range(n-1):
        for j in range(x):
            print('-',end="")
        for j in range(0,y+1 ):
            if j!=y:
               print(chr(il+n-j),end="-")
            else:
              print(chr(il+n-j),end="")  
        for j in range(n-y,n):
            print("-",chr(il+j+1),end="",sep="")
        for j in range(x):
            print('-',end="")
        x+=2
        y-=1
        print()




#problem link:
#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true