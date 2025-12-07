from typing import List

lines = open("input.txt").read().splitlines()
grid = [list(line) for line in lines]
start = lines[0].index('S')

# p1
# def F(x: int, y: int, grid: List[List[str]], visited: List[List[bool]]) -> int:
#     if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
#         return 0
#     if visited[x][y]:
#         return 0
    
#     visited[x][y] = True
#     cnt = 0
    
#     if grid[x][y] == '^':
#         cnt += 1
#         cnt += F(x, y - 1, grid, visited)
#         cnt += F(x, y + 1, grid, visited)
#     else:
#         cnt += F(x + 1, y, grid, visited)
    
#     return cnt

# visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
# res = F(0, start, grid, visited)
# print(res)

# p2
dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
dp[0][start] = 1
for i in range(1, len(dp)):
    for j in range(len(dp[0])):
        if grid[i][j] == '^':
            if j > 0:
                dp[i][j - 1] += dp[i - 1][j]
            if j < len(dp[0]) - 1:
                dp[i][j + 1] += dp[i - 1][j]
        else:
            dp[i][j] += dp[i - 1][j]

print(sum(dp[-1]))