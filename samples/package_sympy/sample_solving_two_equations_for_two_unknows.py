from sympy import solve
from sympy.abc import x, y


# Sample: Solving Two Equations for Two Unknows
# -4x + 3y - 2 = 0
# -3x + 2y + 4 = 0
# Result: {x: 16, y: 22}

result = solve([(-4)*x + 3*y - 2, (-3)*x + 2*y + 4], x, y)
print(result)  # {x: 16, y: 22}
