from queue import PriorityQueue
v = 6
graph = [[] for i in range(v)]
def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
def bestFitSearch(source, target, n):
    visited = [False] * n
    pq = PriorityQueue()
    pq.put((0, source))
    visited[source] = True
    while pq.empty() == False:
        u = pq.get()[1]
        print(u, end=" ")
        if u == target:
            break
        for v, c in graph[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    print()
# Adding edges to the graph
addedge(0, 1, 1)
addedge(0, 2, 2)
addedge(0, 3, 3)
addedge(1, 4, 4)
addedge(2, 5, 5)
source = 0
target = 5

# Running the Best Fit Search algorithm
bestFitSearch(source, target, v)