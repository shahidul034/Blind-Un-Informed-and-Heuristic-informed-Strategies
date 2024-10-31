from collections import deque, defaultdict
def bfs(start, node, adj_list):
    visited=defaultdict(int)
    label=defaultdict(int)
    q=deque()
    label[start]=0
    q.append(start)
    visited[start]=1
    while q:
        u=q.popleft()
        for v in adj_list[u]:
            if not visited[v]:
                visited[v]=1
                label[v]=label[u]+1
                q.append(v)
    for i in range(1, node+1):
        print(f"distance from node {start} to {i} is {label[i]}\n")
adj_list = {1: [2, 3], 2: [1, 4], 3: [1], 4: [2]}
bfs(1, 4, adj_list)