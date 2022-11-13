#Шаг1. загадать случайное число
import random

number = random.randint(1, 100)
#print(number)
while True:
    #шаг2. Предложить пользователю ввести число
    user_number = int(input('введите число: '))
    #Шаг3. сравнение чисел. Вывод результата
    if number == user_number:
        print('Победа')
        break
    elif number < user_number:
        print('Ваше число больше загаданного')
    else:
        print('Ваше число меньше загаданного')
