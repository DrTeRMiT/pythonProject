print('соревнования по PYTHON')
count = int(input('введите количество участников:'))
i = count
members = []
while i > 0:
    name = input('Кто занял {} место?' .format(i))
    members.append(name)
    i-=1

#кто учавствовал в соревновании. (по алфавиту)
print ('В соревновании учавствовали: ', sorted(members))

    # мы записали людей с конца?
members.reverse()

    #нам нужно взять первые 3 места
result = members[:3]

result = 'Победители: {}. Поздравляем!'.format(result)
print(result)