if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input("Enter a name: ")
    
    print(student_marks)
    
    marks = student_marks.get(query_name)
    num = float((marks[1]+marks[2]+marks[0])/3);
    decimal = "{:.2f}".format(num)
    print(decimal)
    
    # num = student_marks.get(query_name)
    # print(type(num))