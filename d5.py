lines = open("input.txt").read().split("\n")
ranges, queries = [], []

def collapse_range(ranges):
    ranges.sort()
    collapsed = []
    current_start, current_end = ranges[0]

    for start, end in ranges[1:]:
        if start <= current_end + 1:
            current_end = max(current_end, end)
        else:
            collapsed.append((current_start, current_end))
            current_start, current_end = start, end

    collapsed.append((current_start, current_end))
    return collapsed

for i in range(len(lines)):
    if lines[i] == "":
        break
    N, M = map(int, lines[i].split("-"))
    ranges.append((N, M))

for j in range(i + 1, len(lines)):
    queries.append(int(lines[j]))

final_ranges = collapse_range(ranges)
cnt = 0

# p1
# for q in queries:
#     for start, end in final_ranges:
#         if start <= q <= end:
#             cnt += 1
#             break

# p2
for start, end in final_ranges:
    cnt += end - start + 1

print(cnt)