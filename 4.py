a = int(input())
b = 0
c = 0
while a > 0: 
    
    if a > c: 
        c = a
        b += 1
        a = int(input())

    elif a == c:
        c = a
        b += 0
        a = int(input())

    elif a < c:
        c = a
        b = 1
        a = int(input()) 

print(b)