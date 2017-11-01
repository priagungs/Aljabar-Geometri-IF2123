import matrixOp
import math

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

def MStretch(var, k):
    if var == 'x':
        return [[k,0], [0,1]]
    elif var == 'y':
        return [[1,0], [0,k]]

def stretch(var, k):
    M = MStretch(var, k)
    for i in range(len(vertices)):
        #vertices in accordance to origin point
        vertices[i][0] -= centerPointX
        vertices[i][1] -= centerPointY

        #dilation process
        vertices[i] = matrixOp.multiply(M, vertices[i])

        #vertices in accordance to center point
        vertices[i][0] += centerPointX
        vertices[i][1] += centerPointY

def MRotate(degree):
    rad = math.radians(degree)
    return [[math.cos(rad), -1*math.sin(rad)], [math.sin(rad), math.cos(rad)]]

def rotate(degree, x0, y0):
    translate(-x0, -y0)
    M = MRotate(degree)
    for i in range(len(vertices)):
        #vertices in accordance to origin point
        vertices[i][0] -= centerPointX
        vertices[i][1] -= centerPointY

        #dilation process
        vertices[i] = matrixOp.multiply(M, vertices[i])

        #vertices in accordance to center point
        vertices[i][0] += centerPointX
        vertices[i][1] += centerPointY
    translate(x0, y0)

# def shear(var, k):
#     if var == 'x':
#         for i in range(len(vertices)):
#             x = vertices[i][0] - centerPointX
#             x = x*(k+1) + centerPointX
#             y = vertices[i][1]
#             temp = [x,y]
#             vertices[i].append(temp)
#     elif var == 'y':
#         for i in range(len(vertices)):
#             x = vertices[i][0]
#             y = vertices[i][1] - centerPointY
#             y = y*(K+1) + centerPointY
#             temp = [x,y]
#             vertices[i].append(temp)
