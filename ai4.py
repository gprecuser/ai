#DFS
n=int(input("Enter the no of nodes "))
adj=[[] for _ in range(n)]
e=int(input("Enter the no of edges "))
print("Enter the edges : ")
for _ in range(e):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
src=int(input("Enter the src node : "))
vis=[False]*n
path=[]
def dfs(node,adj,vis,path):
   path.append(node)
   vis[node]=True
   for i in adj[node]:
    if not vis[i]:
        dfs(i,adj,vis,path)
dfs(src,adj,vis,path)
print("path is ",path)