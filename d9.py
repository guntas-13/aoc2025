lines = open("input.txt").read().splitlines()
reds = [(int(x), int(y)) for line in lines for x, y in [line.split(",")]]

unique_x = sorted(set(x for x, y in reds))
unique_y = sorted(set(y for x, y in reds))

x_map = {x: i for i, x in enumerate(unique_x)}
y_map = {y: i for i, y in enumerate(unique_y)}

compressed_reds = [(x_map[x], y_map[y]) for x, y in reds]

grid = [["." for _ in range(len(unique_x))] for _ in range(len(unique_y))]

for i in range(len(compressed_reds)):
    x, y = compressed_reds[i]
    grid[y][x] = "#"
    
    if i == len(compressed_reds) - 1:
        this, that = compressed_reds[i], compressed_reds[0]
    else:
        this, that = compressed_reds[i], compressed_reds[i + 1]
    
    if this[0] == that[0]:
        for cy in range(min(this[1], that[1]) + 1, max(this[1], that[1])):
            grid[cy][this[0]] = "X"
    elif this[1] == that[1]:
        for cx in range(min(this[0], that[0]) + 1, max(this[0], that[0])):
            grid[this[1]][cx] = "X"

f = open("out.txt", "w")
for x in grid:
    f.write("".join(x) + "\n")
f.close()

area = 0
for i in range(len(reds)):
    for j in range(i + 1, len(reds)):
        ar = (abs(reds[i][0] - reds[j][0]) + 1) * (abs(reds[i][1] - reds[j][1]) + 1)
        area = max(area, ar)
        
print(area)