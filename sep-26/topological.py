def topological(adj):
    indegree = []
    for i in range(len(adj)):
        indegree.append(0)
        for j in range(len(adj)):
            indegree[i] += adj[j][i]

    for i in range(len(adj)):
        for j in range(len(indegree)):
            if indegree[j] == 0:
                indegree[j] = -1
                print(j, end=' ')
                for k in range(len(adj)):
                    if adj[j][k] == 1:
                        indegree[k] -= 1



n = int(input("Enter no. of job pairs: "))
adj = []
for _ in range(n):
    k = [0] * n
    adj.append(k)

job = []
print("Enter jobs in pairs:")
for _ in range(n):
    l = list(map(int, input().split()))
    job.append(l)

for i in range(n):
    adj[job[i][1]][job[i][0]] = 1

print("order of jobs: ")
topological(adj)
print()

'''
OUTPUT

Enter no. of job pairs: 5
Enter jobs in pairs:
0 1
0 2
3 1
2 3
4 3
order of jobs: 
1 3 4 2 0 
'''