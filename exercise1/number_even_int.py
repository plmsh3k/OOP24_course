#user input
user_input = int(input('Please give an integer: '))
#counting even numbers
num_even = 0
while user_input != 0:
    if user_input % 2 == 0:
        num_even += 1
    user_input = int(input('Please give an integer: '))
print()
print(f'Numbers of negative integers: {num_even}')