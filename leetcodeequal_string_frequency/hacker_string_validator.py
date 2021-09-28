s = input()
s = input()
l = 0
a = 0
d = 0
u = 0
al = 0
for i in s:
    if i.isalnum():
        al += 1
    if i.isalpha():
        a = a + 1
    if i.isdigit():
        d += 1
    if i.islower():
        l += 1
    if i.isupper():
        u += 1

if l > 0:
    print("true")
else:
    print("false")
if a > 0:
    print("true")
else:
    print("false")
if d > 0:
    print("true")
else:
    print("false")
if u > 0:
    print("true")
else:
    print("false")
if al > 0:
    print("true")
else:
    print("false")