from random import randint

class Dice:
    def __init__(self, side = 1):
        self.side = side
        
        
    def rolling_die(self):
        self.side = randint(1, 6)
        return self.side
    


def main():
    
    
    def creating_list():
        for _ in range(number_rolls):
            dice_list = [Dice() for _ in range(number)]
            list_of_dices.append(dice_list)
    
    def rolling(number):
        for j in range(number):
            for i in range(number):
                list_of_dices[j][i] = list_of_dices[j][i].rolling_die()
            print(f"List number {j+1} of dices: {list_of_dices[j]}")
            sums[j+1] = sum(dice for dice in list_of_dices[j])
        print(sums)
        evaluation(number)
        
    def evaluation(number):
        maximum = {'index': 0, 'max': 0, 'flag' : 0}
        for index in range(number):
            if sums[index+1] > maximum['max']:
                maximum['index'] = index+1
                maximum['max'] = sums[index+1]
            elif sums[index+1] == maximum['max']:
                    maximum['flag'] += 1       
        if maximum['flag'] == 0:
            print(f"The winner is list number {maximum['index']} - sum is {maximum['max']}")   
        else:
            rolling(maximum['flag'])
            
            
            
            
    number_rolls = int(input("Insert number of rolls "))         
    number = int(input("Insert number of dices "))
    list_of_dices = []
    sums = {1:0,2:0,3:0}
    creating_list()
    rolling(number_rolls)
    


main()