# Создаем переменную 'a', значение которой изначально равно 0:
a = 0
n = int(input())
# Создаем цикл:
for i in range(n):
    b = int(input())
# Создаем условие: если переменная 'b' = 0, то к переменной 'a' добавляем 1: 
    if b == 0:
        a += 1
# По завершению цикла проверяем значение переменной 'a' и выводим результат:
if a > 0:
    # Если переменная 'a' больше 0, то выводим "yes":
    print("yes")
else:
    # Иначе - "no":
    print("no")


