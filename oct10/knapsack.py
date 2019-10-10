def knapsack(w, v, C):
    mat = [[0 for _ in range(C+1)] for _ in range(len(w)+1)]

    for i in range(1, (len(w)+1)):
        for j in range(1, (C+1)):
            if j - w[i-1] >= 0:
                if mat[i-1][j] > (v[i-1] + mat[i-1][j - w[i-1]]):
                    mat[i][j] = mat[i-1][j]
                else:
                    mat[i][j] = v[i-1] + mat[i-1][j - w[i-1]]
            else:
                mat[i][j] = mat[i-1][j]
    
    print()
    for i in range(len(w) + 1):
        for j in range(C+1):
            print(mat[i][j], end='\t')
        print()

    return mat[len(v)][C]


w = list(map(int, input("Enter weight array: ").split()))
v = list(map(int, input("Enter value array: ").split()))
C = int(input("Enter the max capacity: "))
print("Max value = ", knapsack(w, v, C))

'''
OUTPUT

Enter weight array: 2 1 3 2
Enter value array: 12 10 20 15
Enter the max capacity: 5

0 0 0 0 0 0
0 0 12 12 12 12
0 10 12 22 22 22
0 10 12 22 30 32
0 10 15 25 30 37
Max value =  37
'''