def sorting(array):
    for item_i in range(len(array)):
        for item_j in range(len(array)-1,item_i,-1):
            if array[item_j].weight() > array[item_j - 1].weight():
                array[item_j], array[item_j - 1] = array[item_j - 1], array[item_j]
    return array


class Item:
    def __init__(self, name, weight):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
        
    def __str__(self):
        return f'{self.__name} ({self.__weight} g)'
  
  
class Suitcase: 
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.suitcase = []
    
    def print_items(self):
        for item in self.suitcase:
            print(item)
    
    def total_weight(self):
        return sum(item.weight() for item in self.suitcase)
    
    def weight(self):
        return self.total_weight()
    
    def add_item(self, item : Item):
        if (item.weight() + self.total_weight()) > self.max_weight:
            pass
        else:
            self.suitcase.append(item)
            
            
    def heaviest_item(self):
        return sorting(self.suitcase)[0]
    
    def __str__(self):
        if len(self.suitcase) == 1:
            return f'{len(self.suitcase)} item ({self.weight()} g)'
        else:
            return f'{len(self.suitcase)} items ({self.weight()} g)'



class CargoHold:
    def __init__(self, max_weight):
          self.max_weight = max_weight
          self.cargohold = []
    
    def total_weight(self):
        return sum(suitcase.weight() for suitcase in self.cargohold)*0.001
        
        
    def empty_space(self):
        return self.max_weight - self.total_weight()
    
    def add_suitcase(self, suitcase : Suitcase):
        if (suitcase.weight()*0.001 + self.total_weight()) > self.max_weight:
            pass
        else:
            self.cargohold.append(suitcase)
    
    def print_items(self):
        for suitcase in self.cargohold:
            suitcase.print_items()
    
    def __str__(self):
        if len(self.cargohold) == 1:
            return f'{len(self.cargohold)} suitcase, space for {self.empty_space()} kg'
        else:
            return f'{len(self.cargohold)} suitcase, spaces for {self.empty_space()} kg'
    
    
    
if __name__ == '__main__':
    user_input = int(input())
    match user_input:
        case 1:   
            book = Item("ABC Book",200)
            phone = Item("Nokia 3210",100)

            print("Name of the book:", book.name())
            print("Weight of the book:", book.weight())

            print("Book:", book)
            print("Phone:", phone)
        case 2:
            book=Item("ABC Book",200)
            phone=Item("Nokia 3210",100)
            brick=Item("Brick",400)
            suitcase=Suitcase(500)
            print(suitcase)
            suitcase.add_item(book)
            print(suitcase)
            suitcase.add_item(phone)
            print(suitcase)
            suitcase.add_item(brick)
            print(suitcase)
        case 3:
            book=Item("ABC Book",200)
            phone=Item("Nokia 3210",100)
            brick=Item("Brick",400)
            suitcase=Suitcase(1000)
            suitcase.add_item(book)
            suitcase.add_item(phone)
            suitcase.add_item(brick)
            print("The suitcase contains the following items:")
            suitcase.print_items()
            combined_weight=suitcase.weight()
            print(f"Combined weight: {combined_weight} g")
        case 4: 
            book=Item("ABC Book",200)
            phone=Item("Nokia 3210",100)
            brick=Item("Brick",400)
            suitcase=Suitcase(1000)
            suitcase.add_item(book)
            suitcase.add_item(phone)
            suitcase.add_item(brick)
            heaviest=suitcase.heaviest_item()
            print(f"The heaviest item: {heaviest}")
        case 5: 
            cargo_hold=CargoHold(100)
            print(cargo_hold)
            book=Item("ABC Book",200)
            phone=Item("Nokia 3210",100)
            brick=Item("Brick",400)
            adas_suitcase=Suitcase(1000)
            adas_suitcase.add_item(book)
            adas_suitcase.add_item(phone)
            peters_suitcase=Suitcase(1000)
            peters_suitcase.add_item(brick)
            cargo_hold.add_suitcase(adas_suitcase)
            print(cargo_hold)
            cargo_hold.add_suitcase(peters_suitcase)
            print(cargo_hold)
        case 6:
            book=Item("ABC Book",200)
            phone=Item("Nokia 3210",100)
            brick=Item("Brick",400)
            adas_suitcase=Suitcase(1000)
            adas_suitcase.add_item(book)
            adas_suitcase.add_item(phone)
            peters_suitcase=Suitcase(1000)
            peters_suitcase.add_item(brick)
            cargo_hold=CargoHold(100)
            cargo_hold.add_suitcase(adas_suitcase)
            cargo_hold.add_suitcase(peters_suitcase)
            print("The suitcases in the cargo hold contain the following items:")
            cargo_hold.print_items()