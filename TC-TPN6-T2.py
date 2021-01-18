import random
from tkinter import *
from tkinter.ttk import *
from functools import partial
import time

def click(mat, fil, col, aux):
    global vec_img
    global img_dorso
    global cont
    global guarda_valores
    global guarda_botones

    mat[fil][col].configure(image=vec_img[aux])
    ventana.update()

    guarda_valores.append(aux)
    guarda_botones.append(mat[fil][col])
    cont -= 1

    if cont == 0:
            if compara_botones(guarda_valores):
                inhabilita_botones(guarda_botones)
                limpia_vectores(guarda_valores, guarda_botones)
                cont = int(2)
                print("Verdadero")
            else:
                mat[fil][col].configure(image=vec_img[aux])
                ventana.update()
                time.sleep(0.6)
                cambia_dorso(guarda_botones)
                limpia_vectores(guarda_valores, guarda_botones)
                cont = int(2)
                print("Falso")



def cambia_dorso(gb):

    guarda_botones[0].configure(image=img_dorso)
    ventana.update()
    guarda_botones[1].configure(image=img_dorso)
    ventana.update()

def inhabilita_botones(gb):
    gb[0].config(state=DISABLED)
    ventana.update()
    gb[1].config(state=DISABLED)
    ventana.update()


def limpia_vectores(gv, gb):
    gv.clear()
    gb.clear()

def compara_botones(gv):
    if gv[0] == gv[1]:
        result = True

    else:
        result = False

    return result

def numerica():
    mat_num = [None] * 4
    for i in range(4):
        mat_num[i] = [None] * 8

    for i in range(16):
        cont = int(0)
        while cont < 2:
            pos_x = random.randint(0, 3)
            pos_y = random.randint(0, 7)
            while mat_num[pos_x][pos_y] != None:
                pos_x = random.randint(0, 3)
                pos_y = random.randint(0, 7)
            if cont < 2:
                mat_num[pos_x][pos_y] = i
                cont += 1
    for i in range(4):
        print(mat_num[i])

    return mat_num


def botones():
    global vec_img
    global m
    global aux

    cont = int(0)
    for fi in range(4):
        for co in range(8):
            aux = m[fi][co]
            m[fi][co] = Button(image=vec_img[m[fi][co]], command=partial(click, m, fi, co, aux))
            m[fi][co].place(x=(100 * co) + 50, y=(100 * fi) + 50, height=100, width=100)
            cont += 1

    return m, vec_img, aux
def botones_dorso():
    global m
    global img_dorso

    for fi in range(4):
        for co in range(8):
            m[fi][co].configure(image=img_dorso)
            ventana.update()

    return m

# -------------------- Programa Principal --------------------


ventana = Tk()
ventana.geometry("900x500")
ventana.title("MemoTest")

vec_img = []
vec_img.append(PhotoImage(file="img/auto1.png"))
vec_img.append(PhotoImage(file="img/conejo.png"))
vec_img.append(PhotoImage(file="img/et.png"))
vec_img.append(PhotoImage(file="img/leopardo.png"))
vec_img.append(PhotoImage(file="img/tortuga.png"))
vec_img.append(PhotoImage(file="img/uno.png"))
vec_img.append(PhotoImage(file="img/dos.png"))
vec_img.append(PhotoImage(file="img/tres.png"))
vec_img.append(PhotoImage(file="img/diamante.png"))
vec_img.append(PhotoImage(file="img/detective.png"))
vec_img.append(PhotoImage(file="img/auto1a.png"))
vec_img.append(PhotoImage(file="img/auto2.png"))
vec_img.append(PhotoImage(file="img/auto2a.png"))
vec_img.append(PhotoImage(file="img/auto3.png"))
vec_img.append(PhotoImage(file="img/auto3a.png"))
vec_img.append(PhotoImage(file="img/tortuga1.png"))

img_dorso = PhotoImage(file="img/bolsaplata.png")

m = numerica()
m, vec, aux = botones()
cont = int(2)

guarda_valores = []
guarda_botones = []


m = botones_dorso()

ventana.mainloop()

