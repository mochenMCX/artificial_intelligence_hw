import csv
edgeFile = 'edges.csv'


def bfs(start, end):
    # Begin your code (Part 1)
    visited = {}
    visited_note = 0
    data = []
    queue = []
    with open('edges.csv', newline='') as file:
        reader = csv.reader(file)
        for a, b, c, d in reader: # start, end, dist, speed-limit
            if a == 'start':
                continue
            data.append([int(a), int(b), float(c), float(d)])
            visited[int(a)] = False
            visited[int(b)]= False
            
    queue.append([start, [start], float(0)]) # node now, path, dist, num_node
    while queue:
        path = []
        node, path, dist= queue[0]
        queue.pop(0)
        for s, e, d, _ in data:
            if visited[e] == True or s != node:
                continue
            path.append(e)
            queue.append([e, path.copy(), dist + d])
            path.pop(len(path)-1)
            if e == end:
                return queue[len(queue)-1][1], queue[len(queue)-1][2], visited_note
            if visited[e] == False:
                visited_note += 1
            visited[e] = True
    return [], 0, 0

    # raise NotImplementedError("To be implemented")
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
