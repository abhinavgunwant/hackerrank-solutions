n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
score = student_marks[query_name]
avg = (score[0] + score[1] + score[2])/3

print("%.2f" % avg)