lines = open("input.txt").read().split("\n\n")

shapes = [line.split(':')[1] for line in lines[:-1]]
shape_areas = [shape.count('#') for shape in shapes]

queries = lines[-1].splitlines()
region_areas, requirements = [], []
for q in queries:
    dim = q.split()[0][:-1]
    w, h = map(int, dim.split('x'))
    region_areas.append(w * h)
    requirements.append(list(map(int, q.split()[1:])))
    
cnt = 0
for i in range(len(region_areas)):
    tot_area = 0
    for a, b in zip(requirements[i], shape_areas):
        tot_area += a * b
    if tot_area <= region_areas[i]:
        cnt += 1

print(cnt)
    