n = int(input())
b = 0
max = 0

while n > max:
    if n >= max:
        max = n
        b += 1
        n = int(input())
    else:
        b += 0
        n = int(input())
print(b)