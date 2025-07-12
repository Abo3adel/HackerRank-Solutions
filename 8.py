if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    x=arr[0]
    y=-101
    
    for i in arr:
        if i>x:
            y=x
            x=i
        elif i>y and i!=x:
            y=i
            
    print(y)




#problem link:
#https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true