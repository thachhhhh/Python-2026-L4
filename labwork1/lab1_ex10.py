def get_divisors(n):
    # A list to store all positive divisors
    divisors = []
    
    # Check numbers from 1 up to n
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
            
    return divisors

# Example test:
num = 12
print(f"The divisors of {num} are: {get_divisors(num)}")
# Output: The divisors of 12 are: [1, 2, 3, 4, 6, 12]