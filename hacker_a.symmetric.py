n1 = int(input("enter for english: "))
l1 = []
e = input().split(" ")
for i in range(n1):
    l1.append(int(e[i]))

n2 = int(input("enter for french: "))
l2 = []
e2 = input().split(" ")
for j in range(n2):
    l2.append(int(e2[j]))
s1 = set(l1)
s2 = set(l2)
d = s1.symmetric_difference(s2)

print(len(d))
