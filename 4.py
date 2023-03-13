a = int(input())
b = 1
c = 0

while a > 0: 



    
    if a > c: 
        c = a
        b += 1
        a = int(input())

    elif a == c:
        c = a
        b = 0
        a = int(input())

    elif a < c:
        c = a
        b += 1
        a = int(input()) 

print(b)


#    1   2
#    7   5
#    7   8
#    9   1
#    1   3
#    0   0