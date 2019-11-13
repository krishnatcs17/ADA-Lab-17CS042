def dijktras(graph, n, src):
    visited = [0 for _ in range(n)] # visited nodes
    dist = [graph[src][i] for i in range(n)] # array of distances from src to each node
    prev = [src for _ in range(n)]
    count = 0

    while count < n-1:
        minimum = 999
        for i in range(n):
            if dist[i] < minimum and visited[i] != 1:
                minimum = dist[i]
                min_index = i
        visited[min_index] = 1
        count += 1

        for j in range(n):
            if (minimum + graph[min_index][j]) < dist[j] and visited[j] != 1:
                dist[j] = minimum + graph[min_index][j]
                prev[j] = min_index

    print("\nCost of shortest paths:")
    for i in range(n):
        if i != src:
            print(src, "->", i, ": cost = ", dist[i], end=', ')
            p = i; path = str(p)
            while p != src:
                p = prev[p]
                path += str(p)
            print("Path:", '->'.join(path[::-1]))


if __name__ == "__main__":
    graph = []
    n = int(input("Number of nodes: "))
    print("Enter the weight matrix: ")
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    src = int(input("Enter the source node: "))

    dijktras(graph, n, src)

'''
OUTPUT

Number of nodes: 7
Enter the weight matrix:
0 3 999 5 999 999 999
3 0 2 1 999 999 999
999 2 0 4 4 999 1
5 1 4 0 999 3 999
999 999 4 999 0 2 5
999 999 999 3 2 0 6
999 999 1 999 5 6 0
Enter the source node: 1

Cost of shortest paths:
1 -> 0 : cost =  3, Path: 1->0
1 -> 2 : cost =  2, Path: 1->2
1 -> 3 : cost =  1, Path: 1->3
1 -> 4 : cost =  6, Path: 1->2->4
1 -> 5 : cost =  4, Path: 1->3->5
1 -> 6 : cost =  3, Path: 1->2->6

'''