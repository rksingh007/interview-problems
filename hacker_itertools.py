'''from itertools import combinations_with_replacement
a = "achk"
s = sorted(a)
l = sorted(list(combinations_with_replacement(s,3)))
print(l)

for i in range(len(l)):

    print(l[i][0]+l[i][1])'''

s = input()
s = sorted(s)
n1 = len(s)
k = int(input())
l = [""]

'''achk'''
while True:
    curr= l[0]
    n2 = len(curr)

    if len(curr)==k:
        break

    for j in range(n1):

        if len(curr)==0 or ord(curr[n2-1])<=ord(s[j]):
           l.append((curr+s[j]))

    l.remove(curr)
    print(l)
for i in l:
    print(i)








