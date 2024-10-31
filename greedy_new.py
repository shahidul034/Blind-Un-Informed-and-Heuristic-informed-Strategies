graph1 = {'Oradea': ['Zerind', 'Sibiu'], 'Zerind': ['Oradea', 'Arad'], 'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
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
graph2 = {'Oradea':{'Zerind':71,'Sibiu':151},'Zerind':{'Oradea':71,'Arad':75},'Arad':{'Zerind':75,'Timisoara':118,'Sibiu':140},'Timisoara':{'Arad':118,'Lugoj':111},'Lugoj':{'Timisoara':111,'Mehadia':70},'Mehadia':{'Lugoj':70,'Dobreta':70},'Dobreta':{'Mehadia':75,'Craiova':120},'Craiova':{'Dobreta':120,'Rimnicu Vilcea':146,'Pitesti':138},'Sibiu':{'Arad':140,'Oradea':151,'Rimnicu Vilcea':80,'Fagaras':99},'Rimnicu Vilcea':{'Sibiu':80,'Craiova':146,'Pitesti':97},'Fagaras':{'Sibiu':99,'Bucharest':221},'Pitesti':{'Bucharest':101,'Rimnicu Vilcea':97,'Craiova':138},'Bucharest':{'Fagaras':211,'Pitesti':101,'Giurgiu':90,'Urziceni':85},'Giurgiu':{'Bucharest':90},'Urziceni':{'Bucharest':85,'Hirsova':98,'Vaslui':142},'Hirsova':{'Urziceni':98,'Eforie':86},'Eforie':{'Hirsova':86},'Vaslui':{'Urziceni':142,'Iasi':92},'Iasi':{'Neamt':87,'Vaslui':92},'Neamt':{'Iasi':87}}

import queue
path=[]
def greedy(start,end):
    path.append(start)
    # print("****:",path)
    print(start)
    if start==end:
        print("****:",path)
        prev=path[0]
        cost_cnt=0
        for x in range(1,len(path)):
            now=path[x]
            cost_cnt+=graph2[prev][now]
            prev=now
        print(cost_cnt)
        return
    v=graph1[start]
    cost=[(x,hsld[x]) for x in v]
    cost_sorted=sorted(cost, key=lambda x: x[1])
    greedy(cost_sorted[0][0],end)
greedy("Arad","Bucharest")




