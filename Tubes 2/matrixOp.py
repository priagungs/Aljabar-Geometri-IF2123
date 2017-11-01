def multiply(M1, M2):
    # iterate through row M1
    result = []
    for i in range(len(M1)):
       result.append(0)
       # iterate through rows of Y
       for k in range(len(M2)):
           result[i] += M1[i][k] * M2[k]
    return result

def addition(M1, M2): #return M1 + M2
    add = []
    for i in range(len(M1)):
        add.append(M1[i] + M2[i])
    return add
