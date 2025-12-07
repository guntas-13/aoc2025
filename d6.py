lines = open("input.txt").read().split("\n")

res = 0

# p1
# elts = []
# for line in lines:
#     elts.append(line.split())

# ops = elts[-1]
# for i in range(len(ops)):
#     ans = 0 if ops[i] == '+' else 1
#     for j in range(len(elts) - 1):
#         if ops[i] == '*':
#             ans *= int(elts[j][i])
#         elif ops[i] == '+':
#             ans += int(elts[j][i])
#     res += ans

# p2
for row in range(len(lines[0])):
    build = ""
    for col in range(len(lines)):
        if lines[col][row] == ' ':
            continue
        else:
            build += lines[col][row]
    if build.strip() == "":
        res += ans
        continue
    if build[-1] == '*':
        op = '*'
        build = build[:-1]
        ans = 1
    elif build[-1] == '+':
        op = '+'
        build = build[:-1]
        ans = 0
    # print(build, op)
    if op == '+':
        ans += int(build)
    if op == '*':
        ans *= int(build)
        
print(res + ans)