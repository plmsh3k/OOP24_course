lunches= {'ordinary': 2.95, 'luxury': 5.9}

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            self.status = True
        else:
            self.status = False
        return self.status

class PaymentTerminal:
    def __init__(self):
        self.funds = 1000
        self.ordinaries = 0
        self.luxuries = 0

    def eat_ordinary(self, payment: float):
        if (payment - lunches['ordinary']) < 0:
            return payment
        else: 
            payment -= lunches['ordinary']
            self.funds += lunches['ordinary']
            self.ordinaries += 1
            return payment

    def eat_luxury(self, payment: float):
        if (payment - lunches['luxury']) < 0:
            return payment
        else: 
            payment -= lunches['luxury']
            self.funds += lunches['luxury']
            self.luxuries += 1
            return payment
    
    
    def eat_ordinary_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(lunches['ordinary']):
            self.ordinaries += 1
            return True
        else:
            return False


    def eat_luxury_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(lunches['luxury']):
            self.luxuries += 1
            return True
        else:
            return False
    
    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount


if __name__ == "__main__":
    number = input()
    match number:
        case '1':
            card = LunchCard(10)
            print("Balance", card.balance)
            result = card.subtract_from_balance(8)
            print("Payment successful:", result)
            print("Balance", card.balance)
            result = card.subtract_from_balance(4)
            print("Payment successful:", result)
            print("Balance", card.balance)
        case '2':
            exactum = PaymentTerminal()

            change = exactum.eat_ordinary(10)
            print("The change returned was", change)

            change = exactum.eat_ordinary(5.9)
            print("The change returned was", change)

            change = exactum.eat_luxury(5.9)
            print("The change returned was", change)

            print("Funds available at the terminal:", exactum.funds)
            print("Ordinary lunches sold:", exactum.ordinaries)
            print("Luxury lunches sold:", exactum.luxuries)
        case '3':
            exactum = PaymentTerminal()

            change = exactum.eat_ordinary(10)
            print("The change returned was", change)

            card = LunchCard(7)

            result = exactum.eat_luxury_lunchcard(card)
            print("Payment successful:", result)
            result = exactum.eat_luxury_lunchcard(card)
            print("Payment successful:", result)
            result = exactum.eat_ordinary_lunchcard(card)
            print("Payment successful:", result)

            print("Funds available at the terminal:", exactum.funds)
            print("Regular lunches sold:", exactum.ordinaries)
            print("Special lunches sold:", exactum.luxuries)
        case '4':
            exactum = PaymentTerminal()

            card = LunchCard(2)
            print(f"Card balance is {card.balance} euros")

            result = exactum.eat_luxury_lunchcard(card)
            print("Payment successful:", result)

            exactum.deposit_money_on_card(card, 100)
            print(f"Card balance is {card.balance} euros")

            result = exactum.eat_luxury_lunchcard(card)
            print("Payment successful:", result)
            print(f"Card balance is {card.balance} euros")

            print("Funds available at the terminal:", exactum.funds)
            print("Ordinary lunches sold:", exactum.ordinaries)
            print("Luxury lunches sold:", exactum.luxuries)