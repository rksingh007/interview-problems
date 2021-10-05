n,m = input().split(" ")
arr = input().split(" ")
setA= input().split(" ")
setB = input().split(" ")
count = 0
for i in arr:
    if i in setA:
        count+=1
    if i in setB:
        count-=1
print(count)


