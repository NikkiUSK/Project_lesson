def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        l = []
        matrix.append(l)
        for j in range(m):
            l.append(value)
    return matrix

r1 = get_matrix(2, 2, 10)
r2 = get_matrix(3, 5, 42)
r3 = get_matrix(4, 2, 13)
print(r1)
print(r2)
print(r3)