adj = list(26)
act = list(26)
vis = list(26)
bad = False
ans = ""
def dfs(u: int):
    act[u] = 1
    vis[u] =1
    for v in adj[u]:
        if act[v] && v^u:
            bad = True
            break
        else:
            if not vis[v]:
                dfs(v)
    act[u]=0
    ans += chr(u+ord('A'))
