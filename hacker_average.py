#Print the average of the marks array for the student
# name provided, showing 2 places after the decimal.
if __name__ == '__main__':
    n = int(input())                     # number of students
    student_marks = {}                   #dictionary
    for _ in range(n):
        name, *line = input().split()          # input name and marks in single line
        scores = list(map(float, line))        # marks stored in list score
        student_marks[name] = scores           # name and scores list added to dictionary
    query_name = input()                       # input the name of student whom which u want to know avg
    marks=student_marks[query_name]            # get the list of marks in to list marks
    avg=sum(marks)/len(marks)
    print(f"{avg:.2f}")                         # print avg approx. 2 decimal places