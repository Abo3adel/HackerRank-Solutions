def arrays(arr):
    for i in  range(len(arr)//2):
        arr[i],arr[len(arr)-i-1]=arr[len(arr)-i-1],arr[i]
        
    b= numpy.array(arr,float)
    return b


#link:
#https://www.hackerrank.com/challenges/np-arrays/problem?isFullScreen=true