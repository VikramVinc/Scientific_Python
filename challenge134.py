from math import sqrt
T = int(input())
for _ in range(T):
    diagonal = int(input())
    side = (3+(sqrt(9 + 8*diagonal)))/2
    print((side).__trunc__())

