string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
n1 = len(string)
n= int(input())
n2 =int( n1/n)
n3= int((n1/n)+1)
l= []
c = 0
j= n
if n1%2==0 :
    if n%2!=0 and n2:
        n2=n3

    for i in range(n2):
        #for k in range(n):
            l.append(string[c:j])

            j= j+n
            c = c+n
if n1%2!=0:
    if n%2!=0 and n1%n!=0:
        n3=n2

    for k in range(n3):
        l.append(string[c:j])
        j+=n
        c=c+n

print(l)
print(n1)
for a in l:
    print(a)


    '''def wrap(string, n):
    n1=len(string)
    s = str()
    s1=[]
    for i in range(n1):
        s=s+string[i]
        
        if (i+1)%n==0:
            print(s)
            s1.append(s)
            s = ''
            
    if string!=0:
        print(s)
        s1.append(s)
    print(s1)'''