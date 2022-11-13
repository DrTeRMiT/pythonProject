import random

user_number = int(input('Введите ваше число (1-100): '))
print()
pc_number = 0
min_num = 1
max_num = 100

while pc_number != user_number:
    pc_number = random.randint(min_num, max_num)

    print(f'Ваше число: {pc_number}?')
    print('------------')

    hint = input('Дай подсказку, "<", ">", "=": ')
    print('------------')

    if hint == '>':
        if pc_number < user_number:
            min_num = pc_number + 1
        else:
            print('А вот и нет :P')
            print()
            max_num = pc_number - 1
    elif hint == '<':
        if pc_number > user_number:
            max_num = pc_number - 1
        else:
            print('А вот и нет :P')
            print()
            min_num = pc_number + 1
    elif hint == '=':
        if pc_number == user_number:
            break
        else:
            print('Врунишка!')
            print()
    else:
        print('Не такие символы просил тебя ввести...')
        print('Введи один из знаков "<" "=" ">"')
        print()
else:
    print('Какой же ты врунишка!')

print('А я угадал! Ура!')
print('Я - классный ПК, умею отгадывать, что ты загадал :P')