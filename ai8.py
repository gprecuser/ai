def is_safe(graph, color, v, c, n):
    for i in range(n):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True
def solve_graph_coloring(graph, n, m):
    color = [0] * n
    def graph_coloring(v):
        if v == n:
            return True
        for c in range(1, m + 1):  
            if is_safe(graph, color, v, c, n):
                color[v] = c
                if graph_coloring(v + 1):
                    return True
                color[v] = 0 
        return False  
    if graph_coloring(0):  
        print("Solution found:")
        for v in range(n):
            print(f"Vertex {v} ---> Color {color[v]}")
    else:
        print("Solution does not exist")
n = int(input("Enter the number of vertices: "))
print("Enter the adjacency matrix (one row at a time, space-separated):")
graph = [list(map(int, input().split())) for _ in range(n)]
m = int(input("Enter the number of colors: "))
solve_graph_coloring(graph, n, m)