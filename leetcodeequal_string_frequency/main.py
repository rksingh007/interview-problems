s = "aaabbbdbcc"
dict = {}
list = []
c = 0
for i in s:
    if i in dict:
        dict[i] = dict[i]+1
    else:
        dict[i] =1
print(dict)

for item in dict.values():
    list.append(item)
    NewList = sorted(list,reverse = True)

while i==o:
    for i in NewList:
        if(NewList[i]>NewList[i]+1):
            NewList[i] = NewList[i]+1

        if(NewList[i]==NewList[i]+1):
            NewList[i]+1 = NewList[i-1]






