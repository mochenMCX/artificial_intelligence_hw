import csv
edgeFile = 'edges.csv'
from queue import PriorityQueue


def ucs(start, end):
    # Begin your code (Part 3)
    re_dist = 0
    datas = []
    visited = []    #put the visited node
    num_visited = 1     #start node
    parent = {}     #parent
    with open('edges.csv', newline='') as file:
        reader = csv.reader(file)
        for s, e, d, speed in reader:
            if s == 'start':
                continue
            #start node, end node, distance, speed
            datas.append([int(s), int(e), float(d), float(speed)])
    queue = PriorityQueue()
    parent[start] = start
    queue.put([0, start, start])
    while not queue.empty():
        node = queue.get()
        if node[1] in visited:
            continue
        visited.append(node[1])
        parent[node[1]] = node[2]
        if node[1] == end:
            re_dist = node[0]
            break
        for data in datas:
            if data[0] == node[1] and data[1] not in visited:
                queue.put([node[0]+data[2], data[1], node[1]])
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
    # End your code (Part 3)


if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
