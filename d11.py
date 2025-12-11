lines = open("input.txt").read().splitlines()

adj = {}
all_nodes = set()
for line in lines:
    nodes = line.split()
    all_nodes.add(nodes[0][:-1])
    for n in nodes[1:]:
        all_nodes.add(n)
    adj[nodes[0][:-1]] = nodes[1:]

def dfs_p1(node: str, dest: str, adj: dict, dp: dict) -> int:
    if (node == dest):
        return 1
    
    if dp[node] != -1:
        return dp[node]
    
    res = 0
    for nb in adj[node]:
        res += dfs_p1(nb, dest, adj, dp)
    
    dp[node] = res
    return res

n = len(all_nodes)
dp = {x: -1 for x in all_nodes}
print(dfs_p1('you', 'out', adj, dp))
# 571

# print(dfs_p1('svr', 'out', adj, dp))
# 683903757252542732