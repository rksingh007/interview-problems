n= int(input())
for i in range(n):
    n1 = int(input())
    lis = list(map(int,input().split(" ")))
    k = 0
    for j in range(n1-1):
        if lis[j]>=lis[j+1]:
            k+=1
        elif lis[j]<=lis[j+1]:
            k+=1
    if k==n1-1:
        print("yes")
    else:
        print("No")
