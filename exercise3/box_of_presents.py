class Present:
    def __init__(self, name, weight):
        self.name = name 
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} ({self.weight} g)"

class Box:
    def  __init__(self):
        self.weight = 0
        
    def add_present(self, present: Present):
        self.weight += present.weight
        
    def total_weight(self):
        return self.weight
    

def main():
    number = input()
    match number:
        case '1':
            book = Present("Ta-Nehisi Coates: The Water Dancer",200)
            print("The name of the present:",book.name)
            print("The weight of the present:",book.weight)
            print("Present:", book)
        case '2':
            book = Present("Ta-Nehisi Coates: The Water Dancer",200)
            box = Box()
            box.add_present(book)
            print(box.total_weight())
            cd = Present("Pink Flyod: Dark Side of the Moon", 50)
            box.add_present(cd)
            print(box.total_weight())
    
main()