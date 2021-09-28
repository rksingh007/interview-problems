n = int(input())
l =[]
for i in range(n):
    j = input().split(" ")
    if j[0]=="insert":
        l.insert(int(j[1]),int(j[2]))
    if j[0]=="remove":
        l.remove(int(j[1]))
    if j[0]=="pop":
        l.pop()
    if j[0]=="sort":
        l.sort()
    if j[0]=="reverse":
        l.reverse()
    if j[0]=="print":
        print(l)
print(j)

