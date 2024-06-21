r = int(input("enter rows"))
c = int(input("enter columns"))
A = []
for i in range(r) :
    x = []
    for j in range(c) :
        x.append(int(input("Enter the value")))
    A.append(x)
for i in range(r) :
    for j in range(c) :
              print(A[i][j],end=" ")
    print()