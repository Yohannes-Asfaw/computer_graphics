from tkinter import *
import pygame
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def sin_of_x():
    glColor3f(1.0, 0.0, 0.0)
    k = np.linspace(-10, 10, 100)
    v = np.sin(k)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(k, v):
        glVertex2f(a, b)
    glEnd()
    glFlush()


def absolute_func():
    glColor3f(1.0, 0.0, 1.0)
    k = np.linspace(-10, 10, 100)
    v = np.abs(k)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(k, v):
        glVertex2f(a, b)
    glEnd()
    glFlush()


def y_equ_2x():
    glColor3f(0.0, 1.0, 0.0)
    x = np.linspace(-10, 10, 100)
    m = 2 * x
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, m):
        glVertex2f(a, b)
    glEnd()
    glFlush()


def square():
    glColor3f(0.0, 1.0, 1.0)
    x = np.linspace(-10, 10, 1000)
    y = np.power(x, 2)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, y):
        glVertex2f(a, b)
    glEnd()
    glFlush()


def qubic():
    glColor3f(0.30, 0.38, 1.0)
    x = np.linspace(-10, 10, 100)
    q = np.power(x, 3)
    glBegin(GL_LINE_STRIP)
    for a, b in zip(x, q):
        glVertex2f(a, b)
    glEnd()
    glFlush()


def logx():
    glColor3f(1.0, 0.0, 0.0)
    d = np.linspace(0.00001, 10, 100)
    c = np.log(d)
    glBegin(GL_LINE_STRIP)
    glColor3f(1.0, 1.0, 0.0)
    for a, b in zip(d, c):
        glVertex2f(a, b)
    glEnd()
    glFlush()


graph_functions = []


def graph():
    def init():
        pygame.init()
        display = (600, 500)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        gluOrtho2D(-10.0, 10.0, -10.0, 10.0)

    def draw():
        glClear(GL_COLOR_BUFFER_BIT)
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
        if "y=sin(x)" in graph_functions:
            sin_of_x()
        if "y=2x" in graph_functions:
            y_equ_2x()
        if "y=|x|" in graph_functions:
            absolute_func()
        if "y=log(x)" in graph_functions:
            logx()
        if "y=x^3" in graph_functions:
            qubic()
        if "y=x^2" in graph_functions:
            square()

    def main():
        init()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return pygame.quit()

            draw()
            pygame.display.flip()
            pygame.time.wait(10)

    main()


def tk():
    tk_window = Tk()
    tk_window.geometry("800x500")
    Label(tk_window, text="Graph Drawer", font='Times 15 italic bold', ).pack(pady=10, )
    function_list_bar = Scrollbar(tk_window)
    list_down_window = Label(tk_window,
                             text="select function to draw a graph",
                             font=("Times New Roman", 15),
                             padx=10, pady=10,)
    list_down_window.pack()
    function_list = Listbox(tk_window, selectmode="multiple",
                            yscrollcommand=function_list_bar.set, )

    function_list.pack(padx=100, pady=10, )

    equations = ["y=sin(x)", "y=|x|", "y=2x", "y=log(x)", "y=x^3", "y=x^2"]

    for func in range(len(equations)):
        function_list.insert(END, equations[func])
        function_list.itemconfig(func, bg="white")

    function_list_bar.config(command=function_list.yview)

    def selected_funcs():
        selected_func = function_list.curselection()
        for func1 in selected_func:
            option = function_list.get(func1)
            graph_functions.append(option)
        graph()
        graph_functions.clear()

    Button(tk_window, text="Draw selected Graphs", command=selected_funcs, bg="yellow").pack(pady=10)

    tk_window.mainloop()


tk()
