import math
import pandas as pd 
import numpy as np
def task(str):
    str = str.split('\n')
    file = []
    for x in str:
        file.append(x.split(','))
    file = np.array(file)
    file = file.astype(int)
    H = 0
    for i in range(len(file)):
        for j in range(len(file[i])):
            if file[i][j]:
                H += file[i][j]/(len(file)-1)*math.log(file[i][j],2)/(len(file)-1)
    return H
