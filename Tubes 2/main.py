# - *- coding: utf- 8 - *-

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from thread import start_new_thread
import transform
import copy
import os
import time

window = 0                                             # glut window number
width, height = 500, 500                               # window size

print "  ==============================================================================="
print "         _____                           ___                        ____         "
print "        /__   \_   _  __ _  __ _ ___    / __\ ___  ___  __ _ _ __  |___ \        "
print "          / /\/ | | |/ _` |/ _` / __|  /__\/// _ \/ __|/ _` | '__|   __) |       "
print "         / /  | |_| | (_| | (_| \__ \ / \/  \  __/\__ \ (_| | |     / __/        "
print "         \/    \__,_|\__, |\__,_|___/ \_____/\___||___/\__,_|_|    |_____|       "
print "                     |___/                                                       "
print "     _   _  _       _                    ___                          _        _ "
print "    /_\ | |(_) __ _| |__   __ _ _ __    / _ \___  ___  _ __ ___   ___| |_ _ __(_)"
print "    //_\\| || |/ _` | '_ \ / _` | '__|  / /_\/ _ \/ _ \| '_ ` _ \ / _ \ __| '__| |"
print "  /  _  \ || | (_| | |_) | (_| | |    / /_\\  __/ (_) | | | | | |  __/ |_| |  | |"
print "  \_/ \_/_|/ |\__,_|_.__/ \__,_|_|    \____/\___|\___/|_| |_| |_|\___|\__|_|  |_|"
print "         |__/                                                                    "
print "                                 by : 13516089"
print "  "
print "                                      13516054"
print "  "
print "  ==============================================================================="
print "  "

transform.inputVertices()
default_vertices = copy.deepcopy(transform.vertices)

def drawPolygon():
    glBegin(GL_POLYGON)
    glColor3f(0,1,0)
    for i in range(len(transform.vertices)):
        x = transform.vertices[i][0]
        y = transform.vertices[i][1]
        glVertex2f(x,y)
    glEnd()

def drawCartesian():
    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    glVertex2f(249,0)
    glVertex2f(249,700)
    glVertex2f(251,0)
    glVertex2f(251,700)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(1,1,1)
    glVertex2f(0, 249)
    glVertex2f(700, 249)
    glVertex2f(0, 251)
    glVertex2f(700, 251)
    glEnd()

def refresh2d(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def reset():
    temp = copy.deepcopy(default_vertices)
    for i in range(len(temp)):
        temp[i][0] = (temp[i][0] - transform.vertices[i][0])/float(transform.factor)
        temp[i][1] = (temp[i][1] - transform.vertices[i][1])/float(transform.factor)

    for j in range(transform.factor):
        for i in range(len(temp)):
            transform.vertices[i][0] += temp[i][0]
            transform.vertices[i][1] += temp[i][1]
        time.sleep(0.01)

def drawThread():
    def draw():                                            # ondraw is called all the time
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
        glLoadIdentity()                                    # reset position
        refresh2d(width, height)

        drawCartesian()
        drawPolygon()
        glutSwapBuffers()


    # initialization
    glutInit()                                             # initialize glut
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)                      # set window size
    glutInitWindowPosition(0, 0)                           # set window position
    window = glutCreateWindow("Transformation Geometry Model")# create window with title
    glutDisplayFunc(draw)                                  # set draw function callback
    glutIdleFunc(draw)                                     # draw all the time
    glutMainLoop()                                         # start everythinguffer()

start_new_thread(drawThread, ())

print "Command :",
inputCommand = raw_input().split()
while(1):
    if inputCommand[0] == "translate":
        transform.translate(float(inputCommand[1]), float(inputCommand[2]))

    elif inputCommand[0] == "dilate":
        transform.dilate(float(inputCommand[1]))

    elif inputCommand[0] == 'stretch':
        transform.stretch(inputCommand[1], float(inputCommand[2]))

    elif inputCommand[0] == 'rotate':
        transform.rotate(float(inputCommand[1]), float(inputCommand[2]), float(inputCommand[3]))

    elif inputCommand[0] == 'reflect':
        transform.reflect(inputCommand[1])

    elif inputCommand[0] == 'shear':
        transform.shear(inputCommand[1], float(inputCommand[2]))

    elif inputCommand[0] == 'custom':
        transform.custom(float(inputCommand[1]),float(inputCommand[2]),float(inputCommand[3]),float(inputCommand[4]))

    elif inputCommand[0] == 'multiple':
        transform.multiple(int(inputCommand[1]))

    elif inputCommand[0] == 'reset':
        reset()
    elif inputCommand[0] == 'exit':
        print "Thanks for using this app :D"
        os._exit(1)
    print "Command :",
    inputCommand = raw_input().split()
