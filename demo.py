import numpy as np

np.zero((2,3)) #建立一個2x3全為0的陣列
np.ones((2,3,4))  #2x3x4全為1的陣列
np.arange(1,10,2)  #一個由1開始,不超過10,間隔值為2的均勻數值數列
np.linspace(0,10,5)  #建一個0~10,均勻的5個數值陣列

a=np.array([1,2,3,4])
#print(a)
b=np.array([(2,5,1,3,4.5),(7,8,9,10)], dtype=float)
#print(b)
c=np.array([[(2.5,1,3,3.5),(7,8,9,10)],[
    (2.5,1,3,4.5),(7,8,9,10)]],dtype=float)
#print(c)
