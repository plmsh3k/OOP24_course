user_input = int(input('Please give an integer: '))
#counting even numbers
summ = 0
while user_input != 0:
    if (user_input % 3 == 0) and (user_input > 0):
        summ += user_input
    user_input = int(input('Please give an integer: '))
print()
print(f'Sum of positive integers divisible by three is: {summ}')