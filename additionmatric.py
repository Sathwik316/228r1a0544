A = [[1, 2],
     [3, 4]]
B = [[1, 2],
     [3, 4]]
c = [[0, 0],
     [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        c[i][j] = A[i][j] + B[i][j]

print(c)