lines = open("input.txt", "r").read().split("\n")

N, M = len(lines), len(lines[0])
grid = [[c for c in line] for line in lines]
rolls = 0
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
# p1
# for x in range(N):
#     for y in range(M):
#         if grid[x][y] == ".":
#             continue
#         neigbours = 0
#         for k in dirs:
#             xx, yy = x + k[0], y + k[1]
#             if 0 <= xx < N and 0 <= yy < M and grid[xx][yy] == "@":
#                 neigbours += 1
#         if neigbours < 4:
#             rolls += 1

while True:
    cnt = 0
    for x in range(N):
        for y in range(M):
            if grid[x][y] == ".":
                continue
            neigbours = 0
            for k in dirs:
                xx, yy = x + k[0], y + k[1]
                if 0 <= xx < N and 0 <= yy < M and grid[xx][yy] == "@":
                    neigbours += 1
            if neigbours < 4:
                cnt += 1
                rolls += 1
                grid[x][y] = "."
    if cnt == 0:
        break

print(rolls)