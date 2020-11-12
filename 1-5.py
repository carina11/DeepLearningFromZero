import numpy as np

# 1.5.2 配列の生成
print("1.5.2")
x = np.array([1.0, 2.0, 3.0])
print("x=" + str(x))
print()

# 1.5.3　NumPyの算術計算
print("1.5.3")
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print("x= \n"+ str(x))
print("y= \n"+ str(y))

#配列の算術演算
print("x+y=\n" + str(x + y))
print("x-y=\n" + str(x - y))
print("x*y=\n" + str(x * y))
print("x/y=\n" + str(x / y))
print()

# 1.5.4　NumPyのN次元配列
print("1.5.4")
A = np.array([[1, 2], [3, 4]])
print("A=\n" + str(A))

B = np.array([[3, 0], [0, 6]])
print("B=\n" + str(B))

#行列の算術演算
print("A+B= \n" + str(A+B))
print("A*B= \n" + str(A*B))
print("10 * A = \n" + str(10*A))
print()

#1.5.5 ブロードキャスト
print("1.5.5")
A = np.array([[1, 2], [3, 4]])
B = np.array([10,20])
print("A = \n" + str(A))
print("B = \n" + str(B))
print("A * B = \n" + str(A*B))
print()

#1.5.6 要素へのアクセス
print("1.5.6")
X = np.array([[51, 55], [14, 19], [0, 4]])
print("X = \n" + str(X))
print("X[0] = \n" + str(X[0]))
print("X[0][1] = \n" + str(X[0][1]))

print("for文によるアクセス\neach row =>")
for row in X:
    print(row)

X = X.flatten()
print("X.flatten() = \n" + str(X))
print("X[np.array[0, 2, 4] = \n" + str(X[np.array([0, 2, 4])]))
