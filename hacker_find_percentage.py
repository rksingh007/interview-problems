n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
b = student_marks[query_name]
c =  (b[0]+b[1]+b[2])/3
#print(c)
print(student_marks)
#print(round(c,2))
print("{0:.2f}".format(c))
