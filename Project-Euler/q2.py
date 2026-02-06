sum_value = 0
fnumbers = list()
fnumbers.extend([1, 2])

number = 2


while number <= 4_000_000:
    if number % 2 == 0:
        sum_value += number
    number = number + fnumbers[-2]
    fnumbers.append(number)

print(sum_value) 
print(fnumbers[1:10])

    