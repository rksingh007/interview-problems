for i in range(int(input())):

    n = int(input())
    lis = list(map(int,input().split(" ")))
    top = int()
    i = 0
    j = n-1

    while (i!=j):
        if lis[i]<=lis[j]:
            top = lis[j]
            if top>=lis[j-1]:
                j-=1
            else:
                break
        else:
           top = lis[i]
           if top>=lis[i+1]:
                i+=1
           else:
               break
    if j==i:
        print("yess")
    else:
        print("no")