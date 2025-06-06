from collections import deque

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A') + i), end = ' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g, j, visited)

def bfs(g, i, visited):
    q = deque([i])

    while q:
        q.popleft()
        for j in range(len(graph)):
            if g[i][j] == 1 and not visited[j]:
                q.append(j)
                visited[j] = 1

visited_dfs = [0 for _ in range(len(graph))]
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 4,  visited_dfs)
print()
bfs(graph, 4,  visited_bfs)

