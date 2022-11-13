#Шаг1. загадать случайное число
import random

number = random.randint(1, 100)
#print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберите уровень сложности: '))
max_count = levels[level]

while number != user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли')
        break
    print(f'Попытка № {count}')
    #шаг2. Предложить пользователю ввести число
    user_number = int(input('введите число: '))
    #Шаг3. сравнение чисел. Вывод результата
    if number < user_number:
        print('Ваше число больше загаданного')
    elif number > user_number:
        print('Ваше число меньше загаданного')
else:
    print('Победа')