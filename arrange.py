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


'''ques 1 - You are given an array of 0s and 1s in random order. Modify the array to segregate 0s 
on left side and 1s on right side of the array. 
input - 01000110 
output -  00000111 '''

num1 =1
num0 =0

for i in arr:
    if arr[i]==num0:
        new_arr0.append(i)
    else:
        new_arr1.append(i)
new_arr = new_arr0 + new_arr1
for idx,value in enumerate(new_arr):
    arr[idx] = value
print(arr)
print(new_arr)
