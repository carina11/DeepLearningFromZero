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

print("2-3-3")

print("AND")
print("0, 0 = %d" %AND(0, 0))
print("0, 1 = %d" %AND(0, 1))
print("1, 0 = %d" %AND(1, 0))
print("1, 1 = %d" %AND(1, 1))
print()

print("NAND")
print("0, 0 = %d" %NAND(0, 0))
print("0, 1 = %d" %NAND(0, 1))
print("1, 0 = %d" %NAND(1, 0))
print("1, 1 = %d" %NAND(1, 1))
print()

print("OR")
print("0, 0 = %d" %OR(0, 0))
print("0, 1 = %d" %OR(0, 1))
print("1, 0 = %d" %OR(1, 0))
print("1, 1 = %d" %OR(1, 1))
print()