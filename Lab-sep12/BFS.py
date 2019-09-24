def bfs(k, visited, que, adj):
    global n
    visited[k] = 1
    que.append(k)
    while len(que) > 0:
        w = que.pop(0)
        for i in range(n):
            if adj[w][i] and visited[i] == 0:
                que.append(i)
                visited[i] = 1
                print(i, end=' ')



n = int(input("Enter no. of nodes: "))
print("Enter elements: ")
adj = []
visited = [0] * n
que = []
for _ in range(n):
    l = list(map(int, input().split()))
    adj.append(l)
k = int(input("Enter start node: "))
print()
bfs(k, visited, que, adj)
print()


'''
OUTPUT

Enter no. of nodes: 5   
Enter elements: 
0 1 1 0 0 
1 0 0 0 0
1 0 0 1 1
0 0 1 0 1
0 0 1 1 0
Enter start node: 0

1 2 3 4 
'''