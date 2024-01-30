class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.people = []
        self.total_height = 0
    
    def is_empty(self):
        return not(self.people)
    
    def add(self, person : Person):
        self.people.append(person)
        self.total_height += person.height
        
    def print_contents(self):
        print(f"There are {len(self.people)} in the room, and their combined height is {self.total_height} cm.")
        for person in self.people:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        shortest_person = min(self.people, key=lambda x: x.height)
        return shortest_person
    
    
    def remove_shortest(self):
        person = self.shortest()
        self.people.pop(self.people.index(person))
        self.total_height -= person.height
        return person
        
        
            
def main():
    number = input()
    while number != '-1':
        match number:
            case '1':
                room = Room()
                print("Is the room empty?", room.is_empty())
                room.add(Person('Lea', 183))
                room.add(Person('Kenya', 172))
                room.add(Person('Ally', 166))
                room.add(Person('Nina', 162))
                room.add(Person('Dorothy', 175))
                print("Is the room empty?", room.is_empty())
                room.print_contents()
            case '2':
                print("Is the room empty?", room.is_empty())
                print('Shortest:', room.shortest().name)
                print()
                room.print_contents()
            case '3':
                removed = room.remove_shortest()
                print(f'Remove from room: {removed.name}')
                print()
                room.print_contents()
        number = input()

main()