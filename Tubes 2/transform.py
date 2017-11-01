import matrixOp

centerPointX, centerPointY = 250, 250
vertices = []

def inputVertices():
    N = input("Input number of vertex : ")
    for i in range(N):
        vertices.append([])
        x,y = raw_input("Insert X,Y : ").split()
        vertices[i].append(int(x)+centerPointX)
        vertices[i].append(int(y)+centerPointY)

def MTranslate(dx,dy): # return matrix translation
    return [dx,dy]

def translate(dx, dy):
    MT = MTranslate(dx,dy)
    for i in range(len(vertices)): #looping as much as number of vertex
        vertices[i] = matrixOp.addition(vertices[i], MT)

def MDilate(k):
    return [[k,0],[0,k]]

def dilate(k):
    M = MDilate(k)
    for i in range(len(vertices)):
        #vertices in accordance to origin point
        vertices[i][0] -= centerPointX
        vertices[i][1] -= centerPointY

        #dilation process
        vertices[i] = matrixOp.multiply(M, vertices[i])

        #vertices in accordance to center point
        vertices[i][0] += centerPointX
        vertices[i][1] += centerPointY

def stretch(var, k):
    if var == 'x':
        for i in range(len(vertices)):
            x = vertices[i][0] - centerPointX
            x = k*x + centerPointX
            y = vertices[i][1]
            temp = [x,y]
            vertices[i].append(temp)
    elif var == 'y':
        for i in range(len(vertices)):
            x = vertices[i][0]
            y = vertices[i][1] - centerPointY
            y = k*y + centerPointY
            temp = [x,y]
            vertices[i].append(temp)

def shear(var, k):
    if var == 'x':
        for i in range(len(vertices)):
            x = vertices[i][0] - centerPointX
            x = x*(k+1) + centerPointX
            y = vertices[i][1]
            temp = [x,y]
            vertices[i].append(temp)
    elif var == 'y':
        for i in range(len(vertices)):
            x = vertices[i][0]
            y = vertices[i][1] - centerPointY
            y = y*(K+1) + centerPointY
            temp = [x,y]
            vertices[i].append(temp)
