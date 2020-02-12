def is_prime(x):
    isPrim = True
    for i in range(2, int((x)**0.5 + 1)):
        if x % i == 0:
            isPrim = False
    return isPrim
print (is_prime(101))