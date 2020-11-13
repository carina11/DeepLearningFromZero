import numpy as np

def AND(x):
    w = np.array([0.5, 0.5])    #weight
    b = -0.7                    #bias
    
    if(b + np.sum(x*w) > 0):    #np.sum(x*w)  is x1*w1 + x2*w2
        return 1
    elif(b + np.sum(x*w) <= 0):
        return 0
    
print("2-3-2\nAND")
#AND関数にnumpy配列にx1, x2を格納したものを渡している
print("0, 0 = %d" %AND(np.array([0, 0])))
print("0, 1 = %d" %AND(np.array([0, 1])))
print("1, 0 = %d" %AND(np.array([1, 0])))
print("1, 1 = %d" %AND(np.array([1, 1])))

    