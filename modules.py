import numpy as np

GRAY_SCALLE_MAX_VALUE = 255

def toGray(mat):
    newMat = []
    for linha in range(len(mat)):
        newMat.append([])
        for coluna in range(len(mat[0])):
            newMat[linha].append(0)
            for canais in range(len(mat[0][0])):
                newMat[linha][coluna] += mat[linha][coluna][canais]
            newMat[linha][coluna] = int(newMat[linha][coluna]/3) 
    return newMat

def asNumpyArray(mat):
    return np.array(mat,np.uint8)

def invertImage(mat):
    newMat = []
    for linha in range(len(mat)):
        newMat.append([])
        for coluna in range(len(mat[0])):
            newMat[linha].append(GRAY_SCALLE_MAX_VALUE - mat[linha][coluna])
    return newMat