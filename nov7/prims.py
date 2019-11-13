def prims(graph, n):
    weight = 0
    vertex = [0]
    edges = []
    for i in range(1, n):
        mini = 9999
        minindex = 9999
        for j in vertex:
            for k in range(n):
                if k in vertex:
                    continue
                if graph[j][k] < mini:
                    mini = graph[j][k]
                    minindex = k
                    edge = (j, k)

        vertex.append(minindex)
        edges.append(edge)
        weight += mini
    print("\nEdges:", edges)
    return weight

if __name__ == "__main__":
    n = int(input("Enter no. of nodes: "))
    graph = []
    print("Enter weight matrix: ")
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    print("\nWeight of MST:", prims(graph, n))

"""
OUTPUT

Enter no. of nodes: 6
Enter weight matrix: 
999 4 4 999 999 999
4 999 2 999 999 999
4 2 999 3 4 2
999 999 3 999 3 999   
999 999 4 3 999 999
999 999 2 999 999 999

Edges: [(0, 1), (1, 2), (2, 5), (2, 3), (3, 4)]

Weight of MST: 14
"""