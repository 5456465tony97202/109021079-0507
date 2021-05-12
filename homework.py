import sys
import random as rand

if __name__ == '__main__':
    if len(sys.argv) > 1:
        rand.seed(sys.argv[1]) 
        wordlist = list(sys.argv[2])
        lenword = len(wordlist)
        encrynum = [0] * lenword
        for i in range(lenword):
            encrynum[i] = i

        rand.shuffle(encrynum)
        #根據打亂後的數字對應文字
        wordencry = [0] * lenword
        tmp = 0 
        for i in encrynum:
            wordencry[tmp] = wordlist[i]
            tmp += 1
        
        worddecry = [0] * lenword
        tmp = 0
        for i in encrynum:
            worddecry[i] = wordencry[tmp]
            tmp += 1

        print(encrynum)
        print(wordencry)
        print(worddecry)
    else:
        print("無資料")