total = 0
for number in range(1, 794_001):
    number_squared = number**2
    if number_squared % 2 == 1:
        total += number_squared
    
print(total)

