def extract_even(l):
    return [num for num in l if num %2 ==0]

list = [1,4,5,-1,10]
even_list = extract_even(list)

print(even_list)