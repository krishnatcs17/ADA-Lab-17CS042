def dfs(adj, i, j, visited):




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


