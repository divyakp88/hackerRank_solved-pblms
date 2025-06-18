#Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade.
if __name__ == '__main__':
    student=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])   #insert in to the student as list(nested list)

    score=[item[1] for item in student]        #list of scores
    unique=sorted(set(score))                  #convert list in to set to remove duplicates and sort
    s_lowest=unique[1]                            #second lowest element will be in index 1
    names=[item[0] for item in student if item[1]==s_lowest]   #list of names having secon lowest grade
    print('\n'.join(sorted(names)))