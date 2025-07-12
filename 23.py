def mutate_string(string, position, character):
    l=list(string)
    l[position]=character
    return "".join(l)


#problem link:
#https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true