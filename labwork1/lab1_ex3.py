import math
#range(start, stop, step)
num = int(input("Enter a number? "))

if (num<=0):
    is_prime = False
else:
    is_prime = True
    for i in range(2,int(math.isqrt(num))+1):
        if num % 1 == 0:
            is_prime = False
if (is_prime):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
