import queue
import math
test = math.inf
graph = {'Oradea': ['Zerind', 'Sibiu'], 'Zerind': ['Oradea', 'Arad'], 'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
         'Timisoara': ['Arad', 'Lugoj'], 'Lugoj': ['Timisoara', 'Mehadia'], 'Mehadia': ['Lugoj', 'Dobreta'],
         'Dobreta': ['Mehadia', 'Craiova'], 'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
         'Sibiu': ['Arad', 'Oradea', 'Rimnicu Vilcea', 'Fagaras'], 'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
         'Fagaras': ['Sibiu', 'Bucharest'], 'Pitesti': ['Bucharest', 'Rimnicu Vilcea', 'Craiova'],
         'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'], 'Giurgiu': ['Bucharest'],
         'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'], 'Hirsova': ['Urziceni', 'Eforie'], 'Eforie': ['Hirsova'],
         'Vaslui': ['Urziceni', 'Iasi'], 'Iasi': ['Vaslui', 'Neamt'], 'Neamt': ['Iasi']}

def BFS(start,lim):
    level = {}
    for x in graph:
        level[x]= 0
    L = queue.Queue()
    visited={}

    L.put(start)
    level[start]=0
    for x in graph:
        visited[x]=0
    visited[start] = 1
    while L.empty() == False:
        u=L.get()
        if level[u]==lim:
            break
        for v in graph[u]:
            if visited[v]== 0 :
                visited[v]=1
                level[v]=level[u]+1
                L.put(v)

    for x in graph:
        print(x,"-->",level[x])



BFS('Arad',5)

