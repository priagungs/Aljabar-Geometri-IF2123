def multiply(M1, M2):
    for i in range(len(X)):
        # iterate through columns of Y
        for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]


def makeMatrix()            
