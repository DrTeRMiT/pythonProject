print("Добро пожаловать в программу: 'Медицинская карта'")
print("Введите пожалуйста Ваши данные: ")
name = input("Введите своё имя: ")
surname = input("Введите фамилию: ")
age = int(input("Введите свой возраст: "))
weith = int(input("Введите свой вес: "))
if age <= 30 or (weith <= 50 and weith >= 120):
    print (name + " Вы в хорошем состоянии, поздравляем!")
elif age >= 30 or (weith <= 50 and weith >= 120):
    print(name + " Вам требуется заняться собой!")
elif age >= 40 or (weith <= 50 and weith >= 120):
    print(name + " Вам требуется врачебный осмотр!")
else:
    print(name + " необходимо уточнить данные")