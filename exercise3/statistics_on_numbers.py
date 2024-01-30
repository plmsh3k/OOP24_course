class NumberStat():
    def __init__(self):
        self.sum_of_numbers = 0
        self.counting = 0
        self.even = 0
        self.odd = 0
    
    def add_number(self, number):
        self.sum_of_numbers += number
        self.counting += 1
        if number % 2 == 0:
            self.even += number
        else:
            self.odd += number
        
    def count_numbers(self):
        return self.counting
    
    def get_sum(self):
        return self.sum_of_numbers
    
    def get_mean(self):
        if self.count_numbers == 0:
            self.average = 0
        else: self.average = self.get_sum() / self.count_numbers()
        return self.average

    def counting_even(self):
        return self.even
    
    def counting_odd(self):
        return self.odd

def main():
    stats = NumberStat()
    print("Please insert integers numbers. After {-1} program will stop: ")
    number = int(input())
    while number != -1:
        stats.add_number(number)
        number = int(input())
    print('Numbers added:', stats.count_numbers())
    print('Sum of numbers:', stats.get_sum())
    print('Mean of numbers:', stats.get_mean())
    print('Sum of even numbers:', stats.counting_even())
    print('Sum of odd numbers:', stats.counting_odd())
    
    
    
main()