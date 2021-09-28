n= int(input())
student = []
student_score = []
for i in range(n):
        name = input()
        score = float(input())
        student.append([name,score])
        student_score.append(score)
student_score.sort()
student.sort()
for j in range(n):
        if student_score[j]>student_score[0]:
                print(student_score[j])
                break
for k in student:
        if k[1]==student_score[j]:
                print(k[0])
print(student)
print(student_score)
