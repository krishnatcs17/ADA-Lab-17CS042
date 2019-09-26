def nQueen(k, n, X):
    for i in range(n):
        if place(k, i, X):
            X[k] = i
            if k == n-1:
                grid = []
                
                for _ in range(n):
                    l = [0] * n
                    grid.append(l)

                print("Solution: ")
                for m in range(n):
                    grid[m][X[m]] = 'Q'

                for a in grid:
                    print(*a)

            else:
                nQueen(k+1, n, X)


def place(k, i, X):
    for j in range(k):
        if X[j] == i or (abs(X[j] - i) == abs(j - k)):
            return False
    return True


n = int(input("Enter no. of queens: "))
X = [0] * n
nQueen(0, n, X)

'''
OUTPUT

Enter no. of queens: 4
Solution: 
0 Q 0 0
0 0 0 Q
Q 0 0 0
0 0 Q 0
Solution: 
0 0 Q 0
Q 0 0 0
0 0 0 Q
0 Q 0 0
'''