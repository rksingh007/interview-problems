import math
'''s = complex(input())
y = abs(s)
print(y)

val= cmath.phase(s)
print(val)
print((math.sqrt(200))/2)
print(cos(45))'''

ab= int(input())
bc = int(input())
hyp = ((ab**2 + bc**2)**.5)/2

deg = (round((math.degrees(math.asin(hyp/bc)))))
print(deg,chr(176))