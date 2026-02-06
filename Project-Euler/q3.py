number = 600851475143
prime = 2
prime_factors = list()

while prime < number/2:
    if number % prime == 0:
        prime_factors.append(prime)
        number /= prime
    else:
        flag = True
        while flag:
            prime+=1
            for primes in set(prime_factors):
                if prime % primes == 0:
                    break
                break    




