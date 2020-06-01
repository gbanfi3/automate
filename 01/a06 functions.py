import random, sys, os, math
from random import *
for j in range(10):
    count = 1
    for j in range(100):
        i = randint(1, 10)
        if i == 3:
            print(count)
            #print("vége 3")
            # sys.exit()
            break
        count += 1
        #print(i)