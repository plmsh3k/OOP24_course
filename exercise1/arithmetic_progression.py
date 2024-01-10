max_value = int(input('Give maximum value: '))
i = 3
numbers = []
sum = 0
sum_square = 0
c = 0
while i < max_value:
    numbers.append(i)
    sum += i
    sum_square += i*i
    c += 1
    i += 3
    
print(f'Procession is: {numbers}')
print(f'Number of terms is: {c}')
print(f'Sum of terms is: {sum}')
print(f'Sum of squared terms is: {sum_square}')
    
    