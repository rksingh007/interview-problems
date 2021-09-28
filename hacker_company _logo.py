s = input()

d = {}
for i in s:
    if i not in d:
        d[i]= 1
    else:
        d[i] = d[i]+1

sort_d = sorted(d.items(), key=lambda x:(x[1],-ord(x[0])), reverse=True)


print(sort_d[0][0] + " "+ str(sort_d[0][1]))
print(sort_d[1][0] + " "+ str(sort_d[2][1]))
print(sort_d[2][0] + " "+ str(sort_d[2][1]))
