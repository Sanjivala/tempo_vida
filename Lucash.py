from datetime import date
from tkinter import *

janela = Tk()
janela.resizable(False, False)
janela.iconbitmap('lucash.ico')
janela.title('Dias de Vida v1.1')
# janela.iconphoto('LSoft.ico')
# janela.geometry('500x300')
janela.config(bg='orange4')

frame = Frame(janela, bg='orange3', width=500, height=300)
frame.pack()

hoje = date.today()
dia, mes, ano = '23', '11', '1993'
resultado = 0


def diasDeVida():
    global dia, mes, ano, resultado
    nascimento1 = (dia + '-' + mes + '-' + ano)
    nascimento = date(int(nascimento1[6:11]), int(nascimento1[3:5]), int(nascimento1[0:2]))
    data = hoje - nascimento
    resultado = ('{}'.format(data.days))


diasDeVida()

lucash = Label(frame, text='Lucash Sanjivala', font=('Lucida Calligraphy', 20, 'bold'),
               fg='#00008B', bg='orange3')
lucash.grid(row=0, column=1, padx=5, pady=5)

info = Label(frame, text='completaste hoje:'.upper(),
             font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 20, 'bold'), fg='white', bg='orange3')
info.grid(row=1, column=1, padx=5, pady=5)

dias = Label(frame, text='{}'.format(resultado), font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 50, 'bold'),
             fg='blue4', bg='orange3')
dias.grid(row=2, column=1, padx=10, pady=5)

vida = Label(frame, text='Dias de Vida'.upper(), font=('Segoe UI, Tahoma, Geneva, Verdana, sans-serif', 20, 'bold'),
             fg='white', bg='orange3')
vida.grid(row=3, column=1, padx=0, pady=5)

janela.mainloop()
