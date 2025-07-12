

# Complete the solve function below.
def solve(s):
    l=list(s)
    l[0]=l[0].upper()
    for i in range(len(l)):
    
       if l[i]==' ':
           l[i+1] =l[i+1].upper()
    s="" .join(l)      
    return s




#problem link:
#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true