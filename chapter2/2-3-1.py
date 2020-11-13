def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp > theta:
        return 1
    elif tmp <= theta:
        return 0

print("2-3-1")
print("AND")
print("0, 0 = %d" %AND(0, 0))
print("0, 1 = %d" %AND(0, 1))
print("1, 0 = %d" %AND(1, 0))
print("1, 1 = %d" %AND(1, 1))