multiples_total = 0
for number in range(1, 1000):
    if (number % 3 == 0) or (number % 5 ==0):
        multiples_total += number

print(multiples_total)
