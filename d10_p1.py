from collections import deque

lines = open("input.txt").read().splitlines()

entities = [line.split() for line in lines]
patterns, buttons = [], []

for entity in entities:
    pattern, button = entity[0][1:-1], entity[1:-1]
    
    n = len(pattern)
    
    main_bmask = 0
    for c in pattern:
        main_bmask = (main_bmask << 1) | (1 if c == '#' else 0)
    patterns.append(main_bmask)
    
    button_bmasks = []
    for b in button:
        bmask = 0
        for c in b[1:-1].split(','):
            bmask |= (1 << (n - 1 - int(c)))
        button_bmasks.append(bmask)
    buttons.append(button_bmasks)

# print([bin(p) for p in patterns])
# print([[bin(b) for b in button_list] for button_list in buttons])

# ['0b110', '0b10', '0b11101']
# [['0b1', '0b101', '0b10', '0b11', '0b1010', '0b1100'], ['0b10111', '0b110', '0b10001', '0b11100', '0b1111'], ['0b111110', '0b100110', '0b111011', '0b11000']]

def bfs(button_masks: list, pattern: int) -> int:
    q = deque([(btn_mask, 1) for btn_mask in button_masks])
    visited = set()
    while q:
        bmask, depth = q.popleft()
        if bmask == pattern:
            return depth
        for next_bmask in button_masks:
            node = next_bmask ^ bmask
            if node not in visited:
                visited.add(node)
                q.append((node, depth + 1))
    return -1

total = 0
for i in range(len(entities)):
    steps = bfs(buttons[i], patterns[i])
    total += steps
    
print(total)