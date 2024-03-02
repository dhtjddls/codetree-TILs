n, m = map(int, input().split())
li = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
vertex_cnt = 0

def dfs(vertex):
    global vertex_cnt
    for cur in li[vertex]:
        if not visited[cur]:
            visited[cur] = True
            vertex_cnt += 1
            dfs(cur)




for _ in range(m):
    a, b = map(int, input().split())
    li[a].append(b)

visited[1] = True
dfs(1)
print(vertex_cnt)