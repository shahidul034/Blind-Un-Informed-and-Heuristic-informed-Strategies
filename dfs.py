from collections import defaultdict
adj_list = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
color={}

def dfs(n,max_depth):
    global color
    for i in range(1, n+1):
        color[i]="white"
    for i in range(1,n+1):
        dfs_visit(i,0,max_depth)



def dfs_visit(node,depth,max_depth):
    print(node)
    color[node] = "gray"
    if depth>max_depth:
        return
    for neighbor in adj_list[node]:
        if color[neighbor] == "white":
            dfs_visit(neighbor, depth+1, max_depth)
    color[node]="black"
dfs(4,2)