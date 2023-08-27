# Define a square matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Initialize variables to store the sums
print(len(matrix))
main_diagonal_sum = 0
secondary_diagonal_sum = 0

# Calculate the sums of the diagonals
for i in range(len(matrix)):
    main_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][len(matrix) - 1 - i]

# Print the sums
print("Sum of the main diagonal:", main_diagonal_sum)
print("Sum of the secondary diagonal:", secondary_diagonal_sum)




