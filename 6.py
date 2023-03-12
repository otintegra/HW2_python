x = int(input())

if x > 2 * 10**9:
    print("too much value")

else:
    if x < 2:
        a = 1
    if x >= 2:
        a = 2
    for i in range(2, x):
        if x % i == 0:
            a += 1
    print(a)
