import pandas as pd 
import numpy as np
def task(str):
    str = str.split('\n')
    file = []
    for x in str:
        file.append(x.split(','))
    file = np.array(file)
    file = file.astype(int)
    file = file.transpose()
    answer = [[],[],[],[],[]]
    for x in file[0]:
        if x not in answer[0]:
            answer[0].append(x)
    for x in file[1]:
        if x not in answer[1]:
            answer[1].append(x)
    i = 0
    for i in range(file[0].size):
        if file[1][i] in file[0]:
            if file[0][i] not in answer[2]:
                answer[2].append(file[0][i])
        i = i + 1
    i = 0
    for i in range(file[0].size):
        if file[0][i] in file[1]:
            if file[1][i] not in answer[3]:
                answer[3].append(file[1][i])
        i = i + 1
    i = 0
    for i in range(file[0].size):
        if file[0][i] in np.delete(file, i):
            if file[1][i] not in answer[4]:
                answer[4].append(file[1][i])
        i = i + 1
    return(answer)
