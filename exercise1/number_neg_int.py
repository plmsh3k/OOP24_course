#user input
user_input = int(input('Please give an integer: '))
#counting negative numbers
num_neg = 0
while user_input != 0:
    if user_input < 0:
        num_neg += 1
    user_input = int(input('Please give an integer: '))
print()
print(f'Numbers of even integers: {num_neg}')