

def dfs(adj, i, j, visited):
    rowNbr = [-1, 0, 0, 1]
    colnbr = [0, -1, 1, 0]

    visited[i][j] = True

    for k in range(4):
        if issafe(adj, i+rowNbr[k], j+colnbr[k], visited):
            dfs(adj, i+rowNbr[k], j+colnbr[k], visited)


adj = []
visited = []
n = int(input("Number of nodes: "))
for i in range(n):
    f = [False] * n
    visited.append(f)

print("Enter elements row by row: ")
for i in range(n):
    l = list(map(int, input().split()))
    adj.append(l)



def countIsland(adj):
    global visited
    count = 0
    for i in range(n):
        for j in range(n):
            if adj[i][j] and visited[i][j] == False:
                dfs(adj, i, j, visited)
                count += 1
    return count


def issafe(adj, i, j, visited):
    global n
    return (i>=0) and (j>=0) and (i<n) and (j<n) and (adj[i][j] and visited[i][j] == False)


print('\nIsland count:', countIsland(adj))


'''
OUTPUT

Number of nodes: 6
Enter elements row by row: 
0 1 0 0 0 1
0 0 0 1 1 0
1 0 0 1 0 0
0 1 0 0 0 1
0 0 1 0 0 1
0 0 0 0 1 0

Island count: 8
'''