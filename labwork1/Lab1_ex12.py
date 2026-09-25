def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            # Print '*' for the border (first/last row or first/last column)
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()  # Move to the next line after completing a row

# Example usage (5 rows x 5 columns to match the lab example):
print_pattern(5, 5)