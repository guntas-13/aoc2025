lines = open("input.txt", "r").read().split("\n")

def p1(s: str) -> int:
    max_right, max_2 = int(s[-1]), -1
    for i in range(len(s) - 2, -1, -1):
        max_right = max(max_right, int(s[i + 1]))
        max_2 = max(max_2, int(s[i] + str(max_right)))
        # print(f"({s[i]}, {max_right})", end=", ")
    return max_2

def p2(s: str, k: int) -> int:
    # first char is largest that has at least k - 1 chars after it
    # then next largest with at least k - 2 chars after it, etc.
    start, n, ans = 0, len(s), ""
    while k > 0:
        end = n - k + 1
        max_val = max(s[start:end])
        start += s[start:].index(max_val) + 1
        k -= 1
        ans += max_val
    
    return int(ans)

cnt = 0
for line in lines:
    # cnt += p1(line)
    cnt += p2(line, 12)

print(cnt)