scores = []
students = []
for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.append(score)
        students.append([name, score])
        
scores.sort()

selScore = -1
selStudents = []

for i in scores:
    if selScore != i and selScore != -1:
        selScore = i
        break
    selScore = i

for student in reversed(students):
    if student[1] == selScore:
        selStudents.append(student[0])
        
selStudents.sort()

for i in selStudents:
    print(i)