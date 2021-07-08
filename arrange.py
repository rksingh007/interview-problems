''' reverse the string without changing the position of special characters . '''
'''def reverse (str):
    n = len(str)
    index = 0
    for i in range():'''
s= "r@gt_gh"
n = len(s)
print(n)
x = list(s)
i=0
j=n-1
while i<j:
    if not x[i].isalpha():
        i+=1
    elif not x[j].isalpha():
        j-=1
    else:
        x[i], x[j] = x[j], x[i]
        i+=1
        j-=1

print(x)

'''ques 3 - Given a String of length S, reverse the whole string without reversing the individual 
words in it. Words are separated by dots. 
A.lazy.dog 
dog.lazy.A '''

y = "lazy.dog.raj.manu"
x = y.split(".")
n=len(x)
i=0
j=n-1
while i<j:
    x[i] , x[j] =x[j], x[i]
    i+=1
    j-=1


print(n)
z ='.'.join(x)
print(z)



