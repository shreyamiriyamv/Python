A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]

output = [[0, 0], [0, 0]]
for row in range(len(A)):
    for col in range(len(A[row])):
        output[row][col] = A[row][col] + B[row][col]

print(output)
