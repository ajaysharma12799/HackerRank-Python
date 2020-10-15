if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_marks = student_marks[query_name]
    a, b, c = query_marks
    print("{0:.2f}".format( (a+b+c)/len(query_marks) ))
    
    # sum = 0
    # average = 0.00
    # for studentNames, studentMarks in student_marks.items():
    #     length = len(studentMarks)
    #     if studentNames == query_name:
    #         for marks in studentMarks:
    #             sum += marks
    #             average = sum/length
    
    # print( round(average, 2) )