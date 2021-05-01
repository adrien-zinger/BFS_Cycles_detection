def run():
    total_shapes = 0
    total_grahes = 0
    e = [input().split() for _ in range(int(input()))]
    while len(e) > 0:
        e, l = __dfs(e)
        total_shapes += l
        total_grahes += 1
    print(f'{total_grahes} {total_shapes}')

def __dfs(e):
    queue = [e[0][0]]
    loop = 0
    visited = {}
    while len(queue) > 0:
        h = queue.pop(0)
        visited[h] = 1
        nexts = [x[(0,1)[h==x[0]]] for x in e if h in x]
        for x in nexts:
            if x in visited:
                if visited[x] == 0:
                    loop += 1
            else:
                visited[x] = 0
                queue.append(x)
    e = [x for x in e if not (x[0] in visited or x[1] in visited)]
    return e, loop
