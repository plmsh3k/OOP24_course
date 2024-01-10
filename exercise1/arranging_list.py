#input of user
user_input = input('numbers: ')
# formatting the string
user_input = user_input.replace(' ','')
arrange_list = user_input.split(',')
#sorting
arrange_list.sort()
print(f'Arranged list: {arrange_list}')