# просим ввести число
# находим наименьшее число, наибольшее число, сумму числел
numbers =[]

for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))