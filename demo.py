import numpy as np
import random as rand


np.zeros((2,3)) #建立一個2x3全為0的陣列
x=np.ones((2,3,4)) * 128  #2x3x4全為1的陣列
#print(x)
np.arange(1,10,2)  #一個由1開始,不超過10,間隔值為2的均勻數值數列
x1=np.linspace(0,10,5)  #建一個0~10,均勻的5個數值陣列


fileName="np.npy"
#with open(fileName,"wb")as fp:
 #   np.save(fp, x1)
with open(fileName,"rb") as fp: #rb寫進去
    x2=np.load(fp)
    print(x2)


np.random.seed(1723) #保持數字每次都一樣
y=np.random.randint(2,135,(2,3))
print(y)
z=y.reshape(1,6)  #reshape調整形狀
print(z)
r=np.random.shuffle(z)  #shuffle,將資料打亂
print(r)


data=list("This is a book")
print(data)
rand.seed(1723)
rand.shuffle(data)
print("".join(data))


'''
a=np.array([1,2,3,4])
#print(a)
b=np.array([(2.5,1,3,4.5),(5,6,7,8)], dtype=float)
#print(b)
c=np.array([[(2.5,1,3,4.5),(5,6,7,8)],[
    (2.5,1,3,4.5),(7,8,9,10)]],dtype=float)
#print(c)
'''