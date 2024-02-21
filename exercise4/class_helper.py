class ListHelper:
    def __init__(self):
        pass
        
    def greatest_frequency(my_list: list):
        answer = {'number' : 0, 'count' : 0}
        my_list.sort()
        index = 0
        frequency = 1
        while index < len(my_list) - 1:
            if my_list[index] == my_list[index + 1]:
                frequency += 1
                index += 1
            else:
                if answer['count'] < frequency:
                    answer['number'] = my_list[index]
                    answer['count'] = frequency
                frequency = 1
                index += 1
        return answer['number']
    
    def doubles(my_list : list):
        answer = []
        my_list.sort()
        index = 0
        frequency = 1
        while index < len(my_list) - 1:
            if my_list[index] == my_list[index + 1]:
                frequency += 1
            else:
                if frequency == 2:
                    answer.append(my_list[index])
                frequency = 1
            index += 1
        return answer[0]
    
    
numbers = [1,1,2,1,3,3,4,5,5,5,6,5,5,5]
print(ListHelper.greatest_frequency(numbers))
print(ListHelper.doubles(numbers))
