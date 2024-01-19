def average(d : dict):
    s = d['result1']  + d['result2'] + d['result3']
    return s/3



def smallest_average(person1: dict, person2: dict, person3: dict):
    if (average(person1) < average(person2)) and (average(person1) < average(person3)):
        return person1
    if (average(person2) < average(person1)) and (average(person2) < average(person3)):
        return person2
    if (average(person3) < average(person2)) and (average(person3) < average(person1)):
        return person3
    
person1 = {'name':'Mary', 'result1': 2, 'result2': 3, 'result3': 3}
person2 = {'name':'Gary', 'result1': 1, 'result2': 5, 'result3': 8}
person3 = {'name':'Larry', 'result1': 3, 'result2': 1, 'result3': 1}

print(smallest_average(person1, person2, person3))