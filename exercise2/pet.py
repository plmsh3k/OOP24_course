class Pet:
    def __init__(self, name : str, species : str, year_of_birth : int):
        self.name = name
        self.species = species
        self.year_of_birth =year_of_birth
        
        
def new_pet(name : str, species : str, year_of_birth : int):
    ans  = Pet(name, species, year_of_birth)
    return ans

fluffy = new_pet("Fluffy", "dog", 2017)
print(fluffy.name)
print(fluffy.species)
print(fluffy.year_of_birth)