from random import randint 

#input values
integers_input = input('numbers:')
strings_input = input('strings:')

#deleting a space symbol from string
integers_input = integers_input.replace(' ','')
strings_input = strings_input.replace(' ','')

#splitting the string in list
integers = integers_input.split(',')
strings = strings_input.split(',')
print(f'Integers: {integers}')
print(f'Strings: {strings}')

generated_list = []
for item in range(10):
    #adding to a list random int in range -1000, 1000
    generated_list.append(randint(-1000,1000))
    
print(f'Generated: {generated_list}')