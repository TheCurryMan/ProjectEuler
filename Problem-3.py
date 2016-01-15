def is_prime(a):
    return all(a % i for i in range(2, a))

greatest = 1

for i in range(2,int(600851475143**0.5)):
    if 600851475143 % i == 0 and is_prime(i):
        greatest = i

print(greatest)

#Answer - 6857