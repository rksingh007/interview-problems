n,m = map(int,input().split(" "))
l = []

for i in range(1,(n//2)+1):
    s = ((i+(i-1))*".|.").center(m,"-")
    print(s)
    l.append(s)
    s=''
print("WELCOME".center(m,"-"))
for j in range(len(l)-1,-1,-1):
    print(l[j])


