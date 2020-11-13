# Matplotlib

# 1.6.1 単純なグラフの描画
import numpy as np
import matplotlib.pyplot as plt

#データの作成
x = np.arange(0, 6, 0.1)    #0-6、0.1刻み
y = np.sin(x)

#グラフの描画
plt.plot(x, y)
plt.savefig("1-6-1.png")



