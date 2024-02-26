from random import randint

class Dice:
    def __init__(self, side = 1):
        self.side = side
        
        
    def roll_dice(self):
        self.side = randint(1, 6)
        return self.side
    



class Player:
    def __init__(self, name, player_id):
        self.name = name
        self.player_id = player_id
        self.dice = Dice()
        self.mammal = None

    def rolling_dice(self):
        return self.dice.roll_dice()
    
    def __str__(self):
        return f'Player {self.player_id} : {self.name}'
    

class Mammal:
    def __init__(self, ID, species, name, size, weight):
        self.ID = ID
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight      




if __name__ == '__main__':
    num = int(input())
    match num:
        case 0: 
            players = {0 : Player('Daniil', 0), 1 : Player('Andre', 1), 2 : Player('Viet', 2)}

            for player_id, player in players.items():
                roll = player.rolling_dice()
                print(f"{player} rolled: {roll}")
        case 1: 
            mammal1 = Mammal(1, "Dog", "Buddy", "Medium", "20kg")
            player1 = Player("Emma", 1)
            player1.mammal = mammal1
            print(player1)
            print("Player's pet:", player1.mammal.name)
        case 2:
            def select_pet_mammal(player):
                pet_options = [
                    Mammal(1, "Dog", "Buddy", "Medium", "20kg"),
                    Mammal(2, "Cat", "Whiskers", "Small", "5kg"),
                    Mammal(3, "Rabbit", "Cottontail", "Small", "2kg")
                ]
                pet_index = player.rolling_dice() + player.rolling_dice() - 2
                if pet_index < len(pet_options):
                    player.mammal = pet_options[pet_index]

            player1 = Player("Alice", 1)
            select_pet_mammal(player1)
            print(player1)
            print("Player's pet:", player1.mammal.name)