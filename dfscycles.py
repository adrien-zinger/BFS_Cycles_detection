def dfscycle():
    pass

def dfsedges():
    # get graph
    e = [input().split() for _ in range(int(input()))]
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
        nexts = [x for x in e if h[1] in x]
        for n in nexts:
            if n[1]==h[1]: locked.append(n[::-1])
            else: locked.append(n)
            e.remove(n)
        nexts = [x for x in locked if h[1]==x[0] and not x[1] in visited]
        if len(nexts)<1:
            loop += 1
        queue = queue + nexts
    print(loop)

