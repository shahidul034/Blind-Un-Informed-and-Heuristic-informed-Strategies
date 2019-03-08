import operator
graph = {'Oradea': ['Zerind', 'Sibiu'], 'Zerind': ['Oradea', 'Arad'], 'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
         'Timisoara': ['Arad', 'Lugoj'], 'Lugoj': ['Timisoara', 'Mehadia'], 'Mehadia': ['Lugoj', 'Dobreta'],
         'Dobreta': ['Mehadia', 'Craiova'], 'Craiova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
         'Sibiu': ['Arad', 'Oradea', 'Rimnicu Vilcea', 'Fagaras'], 'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
         'Fagaras': ['Sibiu', 'Bucharest'], 'Pitesti': ['Bucharest', 'Rimnicu Vilcea', 'Craiova'],
         'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'], 'Giurgiu': ['Bucharest'],
         'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'], 'Hirsova': ['Urziceni', 'Eforie'], 'Eforie': ['Hirsova'],
         'Vaslui': ['Urziceni', 'Iasi'], 'Iasi': ['Vaslui', 'Neamt'], 'Neamt': ['Iasi']}
hsld = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Dobreta': 242, 'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77,
        'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100,
        'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}
dist = {}
fringe = {}

start = 'Arad'
goal = 'Bucharest'
def searGreedy(start,goal):
    if start == goal:
        print("Node found\n")
        return
    print(start,"--",end="")
    while True:
        if start in graph:
            x=graph[start]
            for x1 in x:
                fringe[x1] = hsld[x1]
            fringe1=sorted(fringe.items(),key=operator.itemgetter(1))
            start=fringe1[0][0]
            print(fringe1[0][0],"--",end="")
            fringe.clear()
            fringe1.clear()
            if start==goal:
                return

    return






searGreedy(start,goal)