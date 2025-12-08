class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)

        if rootA != rootB:
            if self.size[rootA] > self.size[rootB]:
                self.parent[rootB] = rootA
                self.size[rootA] += self.size[rootB]
            elif self.size[rootA] < self.size[rootB]:
                self.parent[rootA] = rootB
                self.size[rootB] += self.size[rootA]
            else:
                self.parent[rootB] = rootA
                self.size[rootA] += self.size[rootB]
        
def euclid_dist(r: tuple, c: tuple) -> float:
    return ((r[0] - c[0]) ** 2 + (r[1] - c[1]) ** 2 + (r[2] - c[2]) ** 2) ** 0.5

lines = open("input.txt").read().splitlines()

coords = [tuple(map(int, line.split(","))) for line in lines]
coords = {i: coord for i, coord in enumerate(coords)}

distances = {}
for i in range(len(coords)):
    for j in range(i + 1, len(coords)):
        distances[(i, j)] = euclid_dist(coords[i], coords[j])

sorted_nodes = sorted(distances, key=lambda x: distances[x])

dsu = DSU(len(coords))
# cnt = 0
for u, v in sorted_nodes:
    
    # p1
    # if cnt == 1000:
    #     break
    # cnt += 1
    
    if dsu.find(u) != dsu.find(v):
        dsu.union(u, v)
        
        # p2
        for i in range(len(coords)):
            if dsu.size[i] == len(coords):
                print(coords[u], coords[v], coords[u][0] * coords[v][0])
                break

# p1
# sorted_sizes = sorted(dsu.size, reverse=True)
# print(sorted_sizes[0] * sorted_sizes[1] * sorted_sizes[2])

# for i in range(len(coords)):
#     if dsu.parent[i] == i and dsu.size[i] > 1:
#         print(f"Root: {i}, Size: {dsu.size[i]}")