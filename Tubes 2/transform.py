import matrixop
import math
import time
import copy
import re

centerPointX, centerPointY = 250, 250
vertices = []
factor = 100

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
    x = dx/factor
    y = dy/factor
    for j in range(factor):
        MT = MTranslate(x,y)
        for i in range(len(vertices)): #looping as much as number of vertex
            vertices[i] = matrixop.addition(vertices[i], MT)
        time.sleep(0.01)

def MDilate(k):
    return [[k,0],[0,k]]

def dilate(k):
    c = math.pow(k, 1.0/factor)
    for j in range(factor):
        M = MDilate(c)
        for i in range(len(vertices)):
            #vertices in accordance to origin point
            vertices[i][0] -= centerPointX
            vertices[i][1] -= centerPointY

            #dilation process
            vertices[i] = matrixop.multiply(M, vertices[i])

            #vertices in accordance to center point
            vertices[i][0] += centerPointX
            vertices[i][1] += centerPointY
        time.sleep(0.01)

def MStretch(var, k):
    if var == 'x':
        return [[k,0], [0,1]]
    elif var == 'y':
        return [[1,0], [0,k]]

def stretch(var, k):
    c = math.pow(k, 1.0/factor)
    for j in range(factor):
        M = MStretch(var, c)
        for i in range(len(vertices)):
            #vertices in accordance to origin point
            vertices[i][0] -= centerPointX
            vertices[i][1] -= centerPointY

            #dilation process
            vertices[i] = matrixop.multiply(M, vertices[i])

            #vertices in accordance to center point
            vertices[i][0] += centerPointX
            vertices[i][1] += centerPointY
        time.sleep(0.01)

def MRotate(degree):
    rad = math.radians(degree)
    return [[math.cos(rad), -1*math.sin(rad)], [math.sin(rad), math.cos(rad)]]

def rotate(degree, x0, y0):
    deg = degree/factor
    for j in range(factor):
        # tramslate to center point
        MT = MTranslate(-x0,-y0)
        for i in range(len(vertices)): #looping as much as number of vertex
            vertices[i] = matrixop.addition(vertices[i], MT)

        # rotate in accordance to center point
        M = MRotate(deg)
        for i in range(len(vertices)):
            #vertices in accordance to origin point
            vertices[i][0] -= centerPointX
            vertices[i][1] -= centerPointY

            #dilation process
            vertices[i] = matrixop.multiply(M, vertices[i])

            #vertices in accordance to center point
            vertices[i][0] += centerPointX
            vertices[i][1] += centerPointY

        # tramslate back to default point
        MT = MTranslate(x0,y0)
        for i in range(len(vertices)): #looping as much as number of vertex
            vertices[i] = matrixop.addition(vertices[i], MT)
        time.sleep(0.01) #sleep time for animation purpose

def MShear(param,k):
    if param == 'x':
        return [[1,k], [0,1]]
    elif param == 'y':
        return [[1,0], [k,1]]

def shear(param,k):
    Ms = MShear(param,k/factor)
    for j in range(factor):
        for i in range(len(vertices)):
            #vertices in accordance to origin point
            vertices[i][0] -= centerPointX
            vertices[i][1] -= centerPointY

            #shear process
            vertices[i] = matrixop.multiply(Ms, vertices[i])

            #vertices in accordance to center point
            vertices[i][0] += centerPointX
            vertices[i][1] += centerPointY
        time.sleep(0.01)

def MReflect(param):
    if param == 'x':
        return [[1,0], [0,-1]]
    elif param == 'y':
        return [[-1,0], [0,1]]
    elif param == 'y=x':
        return [[0,1], [1,0]]
    elif param == 'y=-x':
        return [[0,-1], [-1,0]]
    else:
        numlist = re.findall("[-+]?[.]?[\d]+(?:,\d\d\d)*[\.]?\d*(?:[eE][-+]?\d+)?", param)
        return [2*float(numlist[0]), 2*float(numlist[1])]

def reflect(param):
    if ((param == 'x') or (param == 'y') or (param == 'y=x') or (param =='y=-x')):
        MR = MReflect(param)
        temp = copy.deepcopy(vertices) #temp list
        for i in range(len(vertices)):
            #vertices in accordance to origin point
            temp[i][0] -= centerPointX
            temp[i][1] -= centerPointY

            #dilation process
            temp[i] = matrixop.multiply(MR, temp[i])

            #vertices in accordance to center point
            temp[i][0] += centerPointX
            temp[i][1] += centerPointY

            # temp list containing element vertices divides by factor
            temp[i][0] = (temp[i][0] - vertices[i][0])/float(factor)
            temp[i][1] = (temp[i][1] - vertices[i][1])/float(factor)

        #Animate the transformation
        for j in range(factor):
            for i in range(len(vertices)):
                vertices[i][0] += temp[i][0]
                vertices[i][1] += temp[i][1]
            time.sleep(0.01)
    else:
        MR = MReflect(param)
        temp = copy.deepcopy(vertices)
        for i in range(len(vertices)):
            #vertices in accordance to origin point
            temp[i][0] -= centerPointX
            temp[i][1] -= centerPointY

            temp[i][0] *= -1
            temp[i][1] *= -1
            #Reflect process
            temp[i] = matrixop.addition(temp[i], MR)

            #vertices in accordance to center point
            temp[i][0] += centerPointX
            temp[i][1] += centerPointY

            # temp list containing element vertices divides by factor
            temp[i][0] = (temp[i][0] - vertices[i][0])/float(factor)
            temp[i][1] = (temp[i][1] - vertices[i][1])/float(factor)

        #Animate the transformation
        for j in range(factor):
            for i in range(len(vertices)):
                vertices[i][0] += temp[i][0]
                vertices[i][1] += temp[i][1]
            time.sleep(0.01)

def MCustom(a,b,c,d):
    return [[a,b], [c,d]]

def custom(a,b,c,d):
    MC = MCustom(a,b,c,d)
    temp = copy.deepcopy(vertices)
    for i in range(len(vertices)):
        #vertices in accordance to origin point
        temp[i][0] -= centerPointX
        temp[i][1] -= centerPointY

        #dilation process
        temp[i] = matrixop.multiply(MC, temp[i])

        #vertices in accordance to center point
        temp[i][0] += centerPointX
        temp[i][1] += centerPointY

        temp[i][0] = (temp[i][0] - vertices[i][0])/float(factor)
        temp[i][1] = (temp[i][1] - vertices[i][1])/float(factor)

    for j in range(factor):
        for i in range(len(vertices)):
            vertices[i][0] += temp[i][0]
            vertices[i][1] += temp[i][1]
        time.sleep(0.01)

def multiple(N):
    pil = []
    for i in range(N):
        pil.append(raw_input().split())
    for i in range(N):
        if pil[i][0] == "translate":
            translate(float(pil[i][1]), float(pil[i][2]))

        elif pil[i][0] == "dilate":
            dilate(float(pil[i][1]))

        elif pil[i][0] == 'stretch':
            stretch(pil[i][1], float(pil[i][2]))

        elif pil[i][0] == 'rotate':
            rotate(float(pil[i][1]), float(pil[i][2]), float(pil[i][3]))

        elif pil[i][0] == 'reflect':
            reflect(pil[i][1])

        elif pil[i][0] == 'shear':
            shear(pil[i][1], float(pil[i][2]))

        elif pil[i][0] == 'custom':
            custom(float(pil[i][1]),float(pil[i][2]),float(pil[i][3]),float(pil[i][4]))
