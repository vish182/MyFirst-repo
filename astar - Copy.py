h_dist = {
    'A': 11,
    'B': 6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0,
}

Graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E': [('D', 6)],
    'D': [('G', 1)],
    'G': [],
}

def h(n):
    return h_dist[n]

def neighbours(i):
    if i in Graph:
        return Graph[i]
    else:
        return None

def getBestNext(open_list):
    res = 100000
    resKey = '!'
    for node in open_list:
        if open_list[node][0] + open_list[node][1] < res:
            res = open_list[node][0] + open_list[node][1]
            resKey = node

    return resKey

def printPath(pred, source, goal):

    trav = goal

    while trav != source:
        print(trav, end=" <- ")
        trav = pred[trav]

    print(source)


def a_star(node_start, node_goal):

    open_list = {node_start: [0,h(node_start)]}
    closed_list = []
    pred = {}

    while True:

        if len(open_list) == 0:
            return pred

        bestNeighbour = getBestNext(open_list)

        for (nKey, nVal) in Graph[bestNeighbour]:

            if nKey in open_list.keys():
                if open_list[nKey][0] + open_list[nKey][1] > open_list[bestNeighbour][0] + nVal + h_dist[nKey]:
                    open_list[nKey] = [open_list[bestNeighbour][0] + nVal, open_list[nKey][1]]
                    pred[nKey] = bestNeighbour
                else:
                    pass

            elif nKey not in closed_list:
                open_list[nKey] = [open_list[bestNeighbour][0] + nVal, h_dist[nKey]]
                pred[nKey] = bestNeighbour

        open_list.pop(bestNeighbour)
        closed_list.append(bestNeighbour)


path = a_star('A', 'G')

print("Result: ")
printPath(path, 'A', 'G')


