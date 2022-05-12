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
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

def h(n):
    return h_dist[n]

def neighbours(i):
    if i in Graph:
        return Graph[i]
    else:
        return None

def a_star(node_start, node_goal):
    open_list = [node_start]
    closed_list = []
    g = {}
    parent = {}
    g[node_start] = 0
    parent[node_start] = node_start

    while len(open_list) > 0:
        n = None

        for i in open_list:
            if n == None or g[i] + h(i) < g[n] + h(n):
                n = i
        if n == node_goal or Graph[n] == None:
            pass
        else:
            for (m, weight) in neighbours(n):
                if m not in open_list and m not in closed_list:
                    open_list.append(m)
                    parent[m] = n
                    g[m] = g[n] + weight

                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parent[m] = n
                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.append(m)

        if n == None:
            print("Path does not exist")
            return None
        if n == node_goal:
            path = []

            while parent[n] != n:
                path.append(n)
                n = parent[n]
            path.append(node_start)

            path.reverse()
            print(path)
            return path
        open_list.remove(n)
        closed_list.append(n)
    print("Path does not exist")
    return None










a_star('A', 'G')