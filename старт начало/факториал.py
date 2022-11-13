N = int(input('введите число для вычисления факториала: '))
F = 1

for i in range(2, N+1):
    F *=i

print(F)