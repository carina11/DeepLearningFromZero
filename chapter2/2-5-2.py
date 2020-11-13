import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    if(b + np.sum(x * w) > 0):
        return 1
    elif(b + np.sum(x * w) <= 0):
        return 0

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7

    if(b + np.sum(x * w) > 0):
        return 1
    elif(b + np.sum(x * w) <= 0):
        return 0

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3

    if(b + np.sum(x * w) > 0):
        return 1
    elif(b + np.sum(x * w) <= 0):
        return 0

def XOR(x1, x2):
    return AND(NAND(x1, x2), OR(x1, x2))

print("2-5-2")
print("XOR")
print("0, 0 = %d" %XOR(0, 0))
print("0, 1 = %d" %XOR(0, 1))
print("1, 0 = %d" %XOR(1, 0))
print("1, 1 = %d" %XOR(1, 1))
print()