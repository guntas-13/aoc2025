from dataclasses import dataclass
@dataclass
class HorizontalLine:
    y: int
    x1: int
    x2: int
    
    def __init__(self, r1: tuple[int, int], r2: tuple[int, int]):
        self.y = r1[1]
        self.x1 = min(r1[0], r2[0])
        self.x2 = max(r1[0], r2[0])

@dataclass
class VerticalLine:
    x: int
    y1: int
    y2: int
    
    def __init__(self, r1: tuple[int, int], r2: tuple[int, int]):
        self.x = r1[0]
        self.y1 = min(r1[1], r2[1])
        self.y2 = max(r1[1], r2[1])
@dataclass
class Box:
    x: int
    y: int
    h: int
    w: int
    
    def __init__(self, r1: tuple[int, int], r2: tuple[int, int]):
        self.x = min(r1[0], r2[0])
        self.y = min(r1[1], r2[1])
        self.w = abs(r1[0] - r2[0]) + 1
        self.h = abs(r1[1] - r2[1]) + 1
    
    @property
    def area(self) -> int:
        return self.h * self.w
    
    def intersects_horizontal_line(self, line: HorizontalLine) -> bool:
        # Check if horizontal line passes through interior of box
        # Line must be strictly between top and bottom edges
        if not (self.y < line.y < self.y + self.h - 1):
            return False
        # Check if line overlaps box horizontally (segments touching at edges are OK)
        return not (line.x2 <= self.x or line.x1 >= self.x + self.w - 1)
    
    def intersects_vertical_line(self, line: VerticalLine) -> bool:
        # Check if vertical line passes through interior of box
        # Line must be strictly between left and right edges
        if not (self.x < line.x < self.x + self.w - 1):
            return False
        # Check if line overlaps box vertically (segments touching at edges are OK)
        return not (line.y2 <= self.y or line.y1 >= self.y + self.h - 1)

lines = open("input.txt").read().splitlines()
reds = [(int(x), int(y)) for line in lines for x, y in [line.split(",")]]

horizontals, verticals = [], []
for i in range(len(reds)):
    if i != len(reds) - 1:
        this, that = reds[i], reds[i + 1]
    else:
        this, that = reds[i], reds[0]
    if this[0] == that[0]:
        verticals.append(VerticalLine(this, that))
    elif this[1] == that[1]:
        horizontals.append(HorizontalLine(this, that))

ans = 0
for i in range(len(reds)):
    for j in range(i + 1, len(reds)):
        box = Box(reds[i], reds[j])
        
        # p1
        # ans = max(ans, box.area)
        
        # p2
        proceed = True
        for h in horizontals:
            if box.intersects_horizontal_line(h):
                proceed = False
                break
        if proceed:
            for v in verticals:
                if box.intersects_vertical_line(v):
                    proceed = False
                    break
        if proceed:
            # print(reds[i], reds[j], box.area)
            ans = max(ans, box.area)
        
print(ans)