import sys
import random as rand
import numpy as np
if __name__=="__main__":
    if len(sys.argv)>2:
        seedValu=int(sys.argv[1])
        data=list(sys.argv[2])
        rand.seed(seedValu)
        rand.shuffle(data)
        print("".join(data))

data=list("This is a book")
np.random.seed(1723)
rand.shuffle(data)
print("".join(data))

data=list("This is a book")
np.random.seed(1723)
rand.shuffle(data)
print("".join(data))