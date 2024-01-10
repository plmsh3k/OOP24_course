def main():
    phone_book = {}
    command = int(input('command (1 search, 2 add, 3 quit):'))
    while command != 3:
        if (command == 1):
           name = input('name: ')
           if name in phone_book:
               print(phone_book[name])
           else:
               print('no number')
        if (command == 2):
            name = input('name:')
            number = input('number:')
            if name in phone_book:
                phone_book[name] = phone_book[name] + '\n' + number
            else:
                phone_book[name] = number
            print('ok!')
        command = int(input('command (1 search, 2 add, 3 quit):'))
    if (command == 3):
        print('quitting...') 


main()