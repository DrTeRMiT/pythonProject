numbers = [3, 9, 8, 7, 6]
size = 5
first = numbers[0]
second = numbers[0]
if (numbers[1] > first):
    first = numbers[1]
else:
    second = numbers[1]
current_index = 2
while(current_index<size):
    if(numbers[current_index]>first):
        second = first
        first = numbers[current_index]
    else:
        if (numbers[current_index]>second):
            second = numbers[current_index]
        current_index = current_index +1
    print(second)