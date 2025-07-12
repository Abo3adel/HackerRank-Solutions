if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        x=input().split()
        if x[0][0]=='i':
            l.insert(int(x[1]),int(x[2]))
        elif x[0][0]=='a':
            l.append(int(x[1]))
        elif x[0][0]=='p' and x[0][1]=='r':
            print(l)
        elif x[0][0]=='p' and x[0][1]=='o':
            del l[len(l)-1]
        elif x[0][0]=='s' :
            l.sort()
        elif x[0][0]=='r' and x[0][2]=='m':
            l.remove(int(x[1]))
        elif x[0][0]=='r' and x[0][2]=='v':
            l.reverse()



#problem link:
#https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true