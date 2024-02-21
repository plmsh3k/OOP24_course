class Person:
    def __init__(self, name, number = [], address = None):
        self.__name = name
        self.__number = number
        self.__address = address
        
    def name(self):
        return self.__name

    def numbers(self):
        return self.__number
    
    def address(self):
        return self.__address
    
    def add_number(self, number):
        self.__number.append(number)
        
    def add_address(self, address):
        self.__address = address

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = {'number':[], 'address':[]}
        self.__persons[name]['number'].append(number)
        
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = {'number':[], 'address':[]}
        self.__persons[name]['address'].append(address)

    def search_number(self, name: str):
        if not name in self.__persons:
            return None
        if len(self.__persons[name]['number']) == 0:
            return None
        else:
            return self.__persons[name]['number']
    
    def search_address(self, name: str):
        if not name in self.__persons:
            return None
        if len(self.__persons[name]['address']) == 0:
            return None
        else:
            return self.__persons[name]['address']


    def all_info(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__book = PhoneBook()

    def instructions(self):
        print("commands: ")
        print("0 quit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__book.add_number(name, number)
        
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__book.add_address(name, address)

    def search(self):
        name = input("name: ")
        numbers = self.__book.search_number(name)
        addresses = self.__book.search_address(name)
        if numbers == None:
            print("number is unknown")  
        else: 
            for number in numbers:
                print(number)   
        if addresses == None:
            print("address is unknown")  
        else:
            for address in addresses:
                print(address)    

    def run(self):
        self.instructions()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.instructions()



if __name__ == '__main__':
    user_input = int(input())
    match user_input:
        case 1: 
            person = Person('Eric')
            print(person.name())
            print(person.numbers())
            print(person.address())
            person.add_number("040-123456")
            person.add_address('Mannerheimintie 10 Helsinki')
            print(person.numbers())
            print(person.address())
        case 2:
            phonebook = PhoneBook()
            phonebook.add_number("Eric","02-123456")
            print(phonebook.search_number("Eric"))
            print(phonebook.search_number("Emily"))
        case 3: 
            application = PhoneBookApplication()
            application.run()