import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
import logging


try:
    root = tk.Tk()
    root.title('Pedido!')
    root.geometry('500x500')
    root.configure(background='#8B0000')
except BaseException as erro:
    logging.exception(erro)


def mover_botao_1(evento=None):
    try:
        if botao_nao.winfo_exists():
            if evento:
                x, y = evento.x, evento.y
            else:
                x, y = root.winfo_pointerxy()
                x -= root.winfo_rootx()
                y -= root.winfo_rooty()
                
            if abs(x - botao_nao.winfo_x()) < 50 and abs(
                y- botao_nao.winfo_y()) < 40:
                new_x = random.randint(0, root.winfo_width()
                                - botao_nao.winfo_width())
                new_y = random.randint(0, root.winfo_height()
                                - botao_nao.winfo_height())
                botao_nao.place(x=new_x, y=new_y)
    except BaseException as erro:
        logging.exception(erro)

def verificar_posicao_mouse():
    try:
        if botao_nao.winfo_exists():
            mover_botao_1()
        root.after(50, verificar_posicao_mouse)
    except BaseException as erro:
        logging.exception(erro)

def aceitou_pedido():
    try:
        messagebox.showinfo('Pedido Aceito', 'Te adoro, meu lindo! Lanchinho mais tarde?')
    except BaseException as erro:
        logging.exception(erro)

def negou_pedido():
    try:
        messagebox.showinfo('Pedido Negado', 'Por que você não quer?')
    except BaseException as erro:
        logging.exception(erro)


margin = Canvas(root, width=500, bg='#8B0000',
                height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#FFFAFA', text='Vamo ficar juntinho? <3',
                fg='#8B0000', font=('Montserrat', 20, 'bold'))
text_id.pack()
botao_nao = tk.Button(root, text='Não', bg='#ffb3c1', command=negou_pedido, 
                      relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
botao_nao.pack()
root.bind('<Motion>', mover_botao_1)
verificar_posicao_mouse()
botao_sim = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE, bd=3, 
                      command=aceitou_pedido, font=('Montserrat', 14, 'bold'))
botao_sim.pack()
root.mainloop()

