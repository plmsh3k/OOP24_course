lunches= {'ordinary': 2.95, 'luxury': 5.9}

class LunchCard:
    def __init__(self, balance : float, name : str):
        self.balance = balance
        self.name = name
        
    def __str__(self):
        return f"The balance of {self.name}' card is {self.balance} euros"
    
    
    def eat_ordinary(self):
        if (self.balance - lunches['ordinary']) < 0:
            raise TypeError("Insufficient amount of money to complete this transaction") 
        else: 
            self.balance -= lunches['ordinary']
        
    def eat_luxury(self):
        if (self.balance - lunches['luxury']) < 0:
            raise TypeError("Insufficient amount of money to complete this transaction") 
        else: 
            self.balance -= lunches['luxury']
        
    
    def deposit_money(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise TypeError("You are not able to deposit negative amount of money to your account") 
        
        
        
        
def main():
    number = input()
    if number == "1":
        card = LunchCard(50, 'Peter')
        print(card)
        card.eat_ordinary()
        print(card)
        card.eat_luxury()
        print(card)
        card.eat_ordinary()
        print(card)
    if number == "2":
        card = LunchCard(10, 'Peter')
        print(card)
        card.deposit_money(15)
        print(card)
        card.deposit_money(10)
        print(card)
        card.deposit_money(200)
        print(card)
    if number == "3":
        card = LunchCard(10,'Peter')
        print(card)
        card.deposit_money(-15)
        print(card)
    if number == "4":
        card_Peter = LunchCard(10, 'Peter')
        print(card_Peter)
        card_Grace = LunchCard(10, 'Grace')
        card_Grace.eat_ordinary()
        card_Peter.eat_luxury()
        print(card_Grace)
        print(card_Peter)
        card_Peter.deposit_money(20)
        card_Grace.eat_luxury()
        print(card_Grace)
        print(card_Peter)
        card_Grace.deposit_money(50)
        print(card_Grace)
        print(card_Peter)
        
main()
