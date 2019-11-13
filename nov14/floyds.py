def floyds(W, n):
    D = W # Distance matrix that contains shortes path between each nodes
    for k in range(n):
        for i in range(n):
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D


if __name__ == "__main__":
    W = [] # weight matrix
    n = int(input("Enter the no. of nodes: "))
    print("Enter the weight matrix: ")
    for _ in range(n):
        W.append(list(map(int, input().split())))

    D = floyds(W, n)
    print("\nDistance matrix is")
    for row in D:
        print(*row)

'''
OUTPUT

Enter the no. of nodes: 5
Enter the weight matrix:
0 2 999 1 8
6 0 3 2 999
999 999 0 4 999
999 999 2 0 3
3 999 999 999 0

Distance matrix is
0 2 3 1 4
6 0 3 2 5
10 12 0 4 7
6 8 2 0 3
3 5 6 4 0

'''