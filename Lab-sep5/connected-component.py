def dfs(k):
    global visited
    global adj
    global v
    visited[k] = 1
    print(k, end="  ")

    for i  in range(v):
        if adj[k][i] == 1 and visited[i] == 0:
            dfs(i)


v = int(input("Vertices: "))
adj = []
visited = [0] * v
print("Enter elements ")
for i in range(v):
    r = list(map(int, input().split()))
    adj.append(r)

print("\nConnected components: ")
for j in range(v):
    if visited[j] == 0:
        dfs(j)
    print()


'''
OUTPUT

Vertices: 5
Enter elements 
0 1 1 0 0 
1 0 0 0 0
1 0 0 0 0
0 0 0 0 1
0 0 0 1 0

Connected components: 
0  1  2  

3  4  
'''