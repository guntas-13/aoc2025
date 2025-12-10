import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

lines = open("input.txt").read().splitlines()

entities = [line.split() for line in lines]
buttons, joltages = [], []

for entity in entities:
    buttons.append([list(map(int, b[1:-1].split(','))) for b in entity[1:-1]])
    joltages.append(list(eval(entity[-1][1:-1])))

# print(buttons)
# print(joltages)
# [[[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]], [[0, 2, 3, 4], [2, 3], [0, 4], [0, 1, 2], [1, 2, 3, 4]], [[0, 1, 2, 3, 4], [0, 3, 4], [0, 1, 2, 4, 5], [1, 2]]]
# [[3, 5, 4, 7], [7, 5, 12, 7, 2], [10, 11, 11, 5, 10, 5]]

ans = 0

for i in range(len(joltages)):
    n = len(joltages[i])
    btn = len(buttons[i])
    
    # constraint matrix A where A[j][i] = 1 if btn i adds to counter j
    A = np.zeros((n, btn), dtype=int)
    for j, button in enumerate(buttons[i]):
        for counter in button:
            A[counter][j] = 1
    
    # Objective: minimize sum of all button presses (coefficients are all 1)
    # Constraints: A @ x = b (equality constraints)
    b = np.array(joltages[i])
    c = np.ones(btn)
    constraints = LinearConstraint(A, lb=b, ub=b)
    
    # Bounds: x >= 0 (non-negative)
    bounds = Bounds(lb=np.zeros(btn), ub=np.inf)
    integrality = np.ones(btn)  # 1 means integer variable
    
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)
    
    if result.success:
        res = int(round(result.fun))
        ans += res
        # print(res)
        # print(result.x.astype(int))
        # print("----")

print(ans)
    