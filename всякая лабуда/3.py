name = 'Leo'
age = 30

hello_str = 'привет, ' + name + ' тебе ' + str(age) + ' лет'
print(hello_str)

hello_str = 'Привет, %s тебе %d лет' %(name, age)
print (hello_str)

hello_str = 'Привет, {} тебе {}  лет' .format(name, age)
print (hello_str)
