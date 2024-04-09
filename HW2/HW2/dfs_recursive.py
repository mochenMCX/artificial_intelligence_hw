import csv
import sys
edgeFile = 'edges.csv'
sys.setrecursionlimit(5000)
num_visited = 1 #start node
def recursive(data, path, visited, end, dist):
    global num_visited
    for s, e, d, _ in data:
        if visited[e] == True or s != path[len(path)-1]:
            continue
        path.append(e)
        if e == end:
            return path, dist, True
        num_visited += 1
        visited[e] = True
        a, b, c = recursive(data, path, visited, end, dist+d)
        if c:
            return a, b, c
        else:
            path.pop(len(path)-1)
    return [], 0, False

def dfs(start, end):
    # Begin your code (Part 2)
    visited = {}
    data = []
    path = [start]
    dist = float(0)
    with open('edges.csv', newline='') as file:
        reader = csv.reader(file)
        for a, b, c, d in reader: # start, end, dist, speed-limit
            if a == 'start':
                continue
            data.append([int(a), int(b), float(c), float(d)])
            visited[int(a)] = False
            visited[int(b)]= False
    visited[start] = True
    path, dist, _ = recursive(data, path, visited, end, dist)
    return path, dist, num_visited


    # raise NotImplementedError("To be implemented")
    # End your code (Part 2)


if __name__ == '__main__':
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
