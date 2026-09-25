colors = ['green','blue','yellow','black']
user_colors = input("What's your favourite color? ")

if user_colors.lower() in colors:
    index_colors = colors.index(user_colors.lower())
    print(f"The color is in index {index_colors}")
else:
    print(f"The color is not in the index")