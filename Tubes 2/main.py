from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import transform
import copy

window = 0                                             # glut window number
width, height = 500, 500                               # window size

transform.inputVertices()

default_vertices = copy.deepcopy(transform.vertices) #Save the default vertices

def drawPolygon():
    glBegin(GL_POLYGON)
    for i in range(len(transform.vertices)):
        x = transform.vertices[i][0]
        y = transform.vertices[i][1]
        glVertex2f(x,y)
    glEnd()



def drawCartesian():
    glBegin(GL_POLYGON)
    glVertex2f(249,0)
    glVertex2f(249,700)
    glVertex2f(251,0)
    glVertex2f(251,700)
    glEnd()

    glBegin(GL_POLYGON)
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

def draw():                                            # ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()                                    # reset position
    refresh2d(width, height)

    glColor3f(0,0,0.3)
    drawCartesian()
    drawPolygon()
    glutSwapBuffers()

    inputCommand = raw_input().split()
    if inputCommand[0] == "translate":
        transform.translate(int(inputCommand[1]), int(inputCommand[2]))

    elif inputCommand[0] == "dilate":
        transform.dilate(float(inputCommand[1]))

    elif inputCommand[0] == 'stretch':
        transform.stretch(inputCommand[1], float(inputCommand[2]))

    elif inputCommand[0] == 'shear':
        transform.shear(inputCommand[1], float(inputCommand[2]))

    elif inputCommand[0] == 'reset':
        transform.vertices = copy.deepcopy(default_vertices)

    elif inputCommand[0] == 'exit':
        sys.exit("Thanks for using our app :D")



# initialization
glutInit()                                             # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)                      # set window size
glutInitWindowPosition(0, 0)                           # set window position
window = glutCreateWindow("Transformation Geometry Model")# create window with title
glutDisplayFunc(draw)                                  # set draw function callback
glutIdleFunc(draw)                                     # draw all the time
glutMainLoop()                                         # start everythinguffer()
