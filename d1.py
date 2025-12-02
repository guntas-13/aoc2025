lines = open("input.txt", "r").read().split("\n")
pos, cnt = 50, 0

part = int(input())

for line in lines:
    d, s = line[0], int(line[1:])
    if part == 1:
        pos = (pos - s) % 100 if d == 'L' else (pos + s) % 100
        cnt += (pos == 0)
    else:
        turn, left = s // 100, s % 100
        cnt += turn
        if d == 'L':
            if pos != 0 and pos - left < 0:
                cnt += 1
        else:
            if pos + left > 100:
                cnt += 1
        pos = (pos - s) % 100 if d == 'L' else (pos + s) % 100
        cnt += (pos == 0)
        
print(cnt)