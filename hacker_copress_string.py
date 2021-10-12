'''s = input()
d= {}
l=[]
c=0
for i in range(len(s)-1):
    if i not in d:
        d[s[i]]=1
    else:
        d[s[i]]=d[s[i]]+1
    if s[i]!=s[i+1]:

        for k,v in d.items():
            l.append((v,k))
    c+=1
#print(d)
print(l)'''

s = input()
s = list(s)
print(s)
l=[]
item = s[0]
count = 0
for i in s:
    if i==item:
        count+=1
        item = i
    else:
        l.append((count, int((item))))
        count=1
        item = i
l.append((count,(item)))
#print(l)
print(*l)