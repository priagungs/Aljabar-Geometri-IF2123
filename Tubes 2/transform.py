# import matrixOp

centerPointX, centerPointY = 250, 250
vertices = []

def inputVertices():
    N = input("Enter number of polygon : ")
    for i in range(N):
        print "vertex ke-", i+1
        x = input("x : ")
        y = input("y : ")
        x += centerPointX
        y += centerPointY
        vertices.append([x,y])

def translate(dx,dy):
    for i in range(len(vertices)):
        vertices[i][0] += dx
        vertices[i][1] += dy

def dilate(k):
    for i in range(len(vertices)):
        x = vertices[i][0] - centerPointX
        x = k*x + centerPointX
        y = vertices[i][1] - centerPointY
        y = k*y + centerPointY
        temp = [x,y]
        vertices[i].append(temp)

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
