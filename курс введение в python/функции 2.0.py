# abc, min, max, round, sum, enumerate

# модуль числа
print(abs(-7))

# min, max
numbers = (5, 15, 7, 1, -9, 0)
print(max(numbers))
print(min(numbers))

# round
print(round(10.9872, 2))

# sum
print(sum(numbers))

# enumerate
winners = ['Leo', 'Max', 'Kate']
for number, winner in enumerate(winners, 1):
    print(number, winner)
