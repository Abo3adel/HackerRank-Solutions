if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        summ=0
        for i in scores:
            summ+=i
        summ/=len(scores)
        student_marks[name] = summ
    query_name = input()
    print(f"{student_marks[query_name]:.2f}")




#problem link:
#https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true