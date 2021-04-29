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
    # get graph
    locked = []
    h = e.pop(0)
    nexts = [x for x in e if h[0] in x]
    for n in nexts:
        if n[0]==h[0]: locked.append(n[::-1])
        else: locked.append(n)
        e.remove(n)
    locked.append(h)
    queue = [h]
    first = h[0]
    loop = 0
    visited = []
    while len(queue) > 0:
        h = queue.pop()
        visited.append(h[0])
        print(h)
        nexts = [x for x in e if h[1] in x]
        for n in nexts:
            if n[1]==h[1]: locked.append(n[::-1])
            else: locked.append(n)
            e.remove(n)
        nexts = [x for x in locked if h[1]==x[0] and not x[1] in visited]
        if len(nexts)<1:
            loop += 1
        queue = queue + nexts
    return e, loop

