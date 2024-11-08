#DLS
n=int(input("Enter the no of nodes "))
adj=[[] for _ in range(n)]
e=int(input("Enter the no of edges "))
print("Enter the edges : ")
for _ in range(e):
    u,v=map(int,input().split())
    adj[u].append(v)
    adj[v].append(u)
vis=[False]*n
src=int(input("Enter the src node "))
dst=int(input("Enter the dest node "))  #destination
limit=(int(input("Enter the limit : "))) #limit upto search
path=[]
def dls(node,dst,adj,vis,depth,limit,path):
   if depth > limit:
       return False      #base condition
   vis[node]=True
   path.append(node)
   if node==dst:
       return True     #another base condition
   for i in adj[node]:
       if not vis[i]:
           if dls(i,dst,adj,vis,depth+1,limit,path):
                return True
   path.pop()  #backtrack
   return False
if dls(src,dst,adj,vis,0,limit,path):
    print("Path found ",path)
else:
    print("Path not found ")