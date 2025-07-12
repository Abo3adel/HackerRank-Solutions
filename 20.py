def merge_the_tools(string, k):
    # your code goes here
    temp=[]
    x=len(string)//k
    for i in range(len(string)):
        if string[i] not in temp:
            print(string[i],end="")
            temp.append(string[i])
        if (i+1)%k==0:
            temp=[]
            print()




#problem link:
#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true