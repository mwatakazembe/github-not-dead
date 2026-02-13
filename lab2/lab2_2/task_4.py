def transpose_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

print("\nenter the matrix row by row. separate the elements with a space. to complete the entry, enter a blank line.")

matrix = []
while True:
    line = input("row: ")
    if not line:
        break
    
    numbers = line.split()
    row = []
    for num in numbers:
        row.append(int(num))
    matrix.append(row)

transposed = transpose_matrix(matrix)

print("\ntransposed:")
for j in range(len(transposed)):
    print(transposed[j])