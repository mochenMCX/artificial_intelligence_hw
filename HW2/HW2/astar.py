import csv
edgeFile = 'edges.csv'
heuristicFile = 'heuristic.csv'
from queue import PriorityQueue


def astar(start, end):
    # Begin your code (Part 4)
    num_visited = 0
    visited = []
    re_dist = 0
    datas = []
    heuristic = {}
    parent = {}     #store the parent node
    with open('edges.csv', newline='') as file:
        reader = csv.reader(file)
        for s, e, d, speed in reader:
            if s == 'start':
                continue
            datas.append([int(s), int(e), float(d), float(speed)])
    with open('heuristic.csv', newline='') as file:
        reader = csv.reader(file)
        for node, fir, sec, thir in reader:
            if node == 'node':
                continue
            if end == 1079387396:
                heuristic[int(node)] = float(fir)     #for first test
            elif end == 1737223506:
                heuristic[int(node)] = float(sec)     #for second test
            else:
                heuristic[int(node)] = float(thir)    #for third test
    queue = PriorityQueue()
    parent[start] = start
    queue.put([float(0)+heuristic[start], start, start])    #distance, node, parent
    while not queue.empty():
        node = queue.get()
        if node[1] in visited:
            continue
        visited.append(node[1])
        parent[node[1]] = node[2]
        node[0] -= heuristic[node[1]]
        if node[1] == end:
            parent[end] = node[2]
            re_dist = node[0]
            break
        for data in datas:
            if data[0] == node[1] and data[1] not in visited:
                queue.put([node[0]+data[2] + heuristic[data[1]], data[1], node[1]])
                num_visited += 1
    path = []
    trace = end
    while parent[trace] != trace:
        path.append(trace)
        trace = parent[trace]
    path.append(start)
    path.reverse()
    return path, re_dist, num_visited
    # raise NotImplementedError("To be implemented")
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
