a = int(input())
b = 1
c = 1
for i in range(1, a + 1):
    b *= i
    c += 1/b
print(c)
