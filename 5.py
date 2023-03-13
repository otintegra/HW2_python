n = int(input())
b = 0
max = 0

while n > 0:
    if n > max:
        max = n
        b = 0
        n = int(input())
    elif n == max:
        n = max
        b += 1
        n = int(input())
    elif n < max:
        b += 0
        n = int(input()) 
print(b + 1)