import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *
import numpy as np


def init():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 0.0, 0.0)

    glBegin(GL_LINE_STRIP)
    v=np.array([0.3,0.4])
    po=np.array([0.1,0.2])
    t=1
    p=po+(t*v)
    for a, b in zip(po, p):
        glVertex2f(a, b)
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(0.0, 10.0)
    glVertex2f(0.0, -10.0)
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(10.0, 0.0)
    glVertex2f(-10.0, 0.0)
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    v1 = np.array([-0.2,0])
    po1 = np.array([0.1, -0.1])
    t1 = 1
    p1 = po1+ (t1 * v1)
    for a, b in zip(po1, p1):
        glVertex2f(a, b)
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    v2 = np.array([0.2, 0])
    po2 = np.array([-0.1, 0.1])
    t2 = 1
    p2 = po2 + (t2 * v2)
    for a, b in zip(po2, p2):
        glVertex2f(a, b)
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    v3 = np.array([0, -0.2])
    po3 = np.array([0.1, 0.1])
    t3= 1
    p3 = po3+ (t3 * v3)
    for a, b in zip(po3, p3):
        glVertex2f(a, b)
    glEnd()
    glFlush()
    glBegin(GL_LINE_STRIP)
    v4= np.array([0, 0.2])
    po4 = np.array([-0.1, -0.1])
    t4 = 1
    p4 = po4 + (t4 * v4)
    for a, b in zip(po4, p4):
        glVertex2f(a, b)
    glEnd()
    glFlush()







def main():
    init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        draw()
        pygame.display.flip()
        pygame.time.wait(10)


main()
