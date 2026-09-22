import math
sum =0
num = int(input("Enter a number? "))
if (num <=0):
    is_perfect = False
else:
    is_perfect = True

    for i in range(1,num):
        if(num % i ==0):
            sum += i
    if(sum != num):
        is_perfect = False
if(is_perfect == False):
    print(f"{num} is not a perfect number")
else:
    print(f"{num} is a perfect number")
    
