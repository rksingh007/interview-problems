s,k = input().split(" ")
s= sorted(s)
l = [""]
s1= ""
count = 0
while True:
    curr = l[count]
    n2 = len(curr)

    if len(curr)==int(k):
        break

    for i in range(len(s)):

        if (len(curr)==0 or ord(curr[n2-1])<=ord(s[i])) and (s[i] not in curr):

            s1 = curr+s[i]
            l.append(s1)
    count+=1
print(l)
print(len(l))
for j in l:
    print(j)