a = int(input())

k = 0
s = 0

while a > 0:
    s += a
    k += 1
    a = int(input())
x = s/k
print(x)
