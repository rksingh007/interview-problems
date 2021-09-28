x=int(input())
y=int(input())
z=int(input())
n=int(input())
list=[]
for i in range (x+1):
    for j in range (y+1):
        for k in range(z+1):
            list.append([i,j,k])
            if (i + j + k == n):
                list.remove([i,j,k])

print(list)
