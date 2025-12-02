import re

def check_p1(n: int) -> int:
    l = len(str(n))
    if l % 2 == 0 and str(n)[: l // 2] == str(n)[l // 2 :]:
            return n
    return 0

def check_p2(n: int) -> int:
    # if re.fullmatch(r'(.+)\1+', str(n)):
    #     return n
    s = str(n)
    if s in (s + s)[1:-1]:
        return n
    return 0

lines = open("input.txt", "r").read().split(",")
cnt = 0

for line in lines:
    l, r = line.split("-")
    for i in range(int(l), int(r) + 1):
        # cnt += check_p1(i)
        cnt += check_p2(i)
print(cnt)