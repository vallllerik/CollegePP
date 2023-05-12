def task(first, second, third):
    A, B, C, D, E, F, G = map(int, first.split())
    print(A + B + C - F + D + E - G)
    A, B, C, D, E, F, G = map(int, second.split())
    print(A + B + C - F + D + E - G)
    A, B, C, D, E, F, G = map(int, third.split())
    print(A + B + C - (F + D + E - G))

print(task())