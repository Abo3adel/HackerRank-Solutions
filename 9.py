if __name__ == '__main__':
    arr=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([score,name])
    arr.sort()
    x=arr[0][0]
    for i in arr:
        if i[0]>x:
            x=i[0]
            break
            
    for i in arr:
        if x==i[0]:
            print(i[1])


#problem link:
#https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true