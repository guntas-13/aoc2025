lines = open("input.txt").read().splitlines()

adj = {}
all_nodes = set()
for line in lines:
    nodes = line.split()
    all_nodes.add(nodes[0][:-1])
    for n in nodes[1:]:
        all_nodes.add(n)
    adj[nodes[0][:-1]] = nodes[1:]

def dfs(node: str, dest: str, adj: dict, dp: dict) -> int:
    if (node == dest):
        return 1
    
    if dp[node] != -1:
        return dp[node]
    
    res = 0
    if node in adj:
        for nb in adj[node]:
            res += dfs(nb, dest, adj, dp)
    
    dp[node] = res
    return res

n = len(all_nodes)
print(dfs('you', 'out', adj, {x: -1 for x in all_nodes}))
# 571

print(dfs('svr', 'out', adj, {x: -1 for x in all_nodes}))
# 683903757252542732

# p2
s2f = dfs('svr', 'fft', adj, {x: -1 for x in all_nodes})
f2d = dfs('fft', 'dac', adj, {x: -1 for x in all_nodes})
d2o = dfs('dac', 'out', adj, {x: -1 for x in all_nodes})

s2d = dfs('svr', 'dac', adj, {x: -1 for x in all_nodes})
d2f = dfs('dac', 'fft', adj, {x: -1 for x in all_nodes})
f2o = dfs('fft', 'out', adj, {x: -1 for x in all_nodes})

print(s2d, d2f, f2o)
# 770085400930 0 3879174736863
print(s2f, f2d, d2o)
# 24087 4368408 4860

# svr -> fft -> dac -> out
p1 = s2f * f2d * d2o
# svr -> dac -> fft -> out
p2 = s2d * d2f * f2o
print(p1 + p2)