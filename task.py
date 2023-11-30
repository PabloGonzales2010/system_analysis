import numpy as np

a = ["a",["s","d"],"f",["g","h","j"],"k","l",";"]
b = ["d",["a","f"],"s","h",["g","j","k"],["l",";"]]

numberOfElements = 0
for i in a:
    if isinstance(i,list):
        numberOfElements += len(i)
    else:
        numberOfElements += 1

hashA = {}
hasht1 = []
hasht2 = []
iter = 0
for i in a:
    if isinstance(i,list):
        for j in i:
            hasht1.append(j)
            hasht2.append(iter)
            iter += 1
    else:
        hasht1.append(i)
        hasht2.append(iter)
        iter += 1
hashA = dict(zip(hasht1, hasht2))
invhashA = {v: k for k, v in hashA.items()}

A = np.zeros((numberOfElements,numberOfElements))
for i in range(len(A)):
    for j in range(len(A[i])):
        if (i == j): A[i][j] = 1
for i in range(len(a)):
    if isinstance(a[i],list):
        for j in range(len(a[i])):
            for k in range(len(a[i])): A[hashA[a[i][j]]][hashA[a[i][k]]] = 1
            for k in range(i,len(a)):
                if isinstance(a[k],list):
                    for l in range(len(a[k])):
                        A[hashA[a[i][j]]][hashA[a[k][l]]] = 1
                else: A[hashA[a[i][j]]][hashA[a[k]]] = 1
    else:
        for k in range(i,len(a)):
            if isinstance(a[k],list):
                for l in range(len(a[k])):
                    A[hashA[a[i]]][hashA[a[k][l]]] = 1
            else: A[hashA[a[i]]][hashA[a[k]]] = 1



print(A)