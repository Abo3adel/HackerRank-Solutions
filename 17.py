

def split_and_join(line):
    l=line.split()
    for i in range(len(l)):
        print(l[i],end="")
        if i!=len(l)-1:
            print('-',end="")
    return ""
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)



#problem link:
#https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true