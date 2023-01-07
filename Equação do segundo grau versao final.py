from tkinter import*
from tkinter import Tk, StringVar, ttk
from tkinter import messagebox

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#3fbfb9"  #verde






def Verifica():
    if coeficiente_a.get() !='' and coeficiente_b.get() !=''  and coeficiente_c.get() !='':
        if float(coeficiente_a.get()) != 0:
            return 1
        if float(coeficiente_a.get()) == 0:
            messagebox.showerror('Erro', 'O Coeficiente "A" não pode ser igual a ZERO:')
            return 0
            
    if coeficiente_a.get() =='' or coeficiente_b.get() =='' or coeficiente_c.get() =='':
        messagebox.showerror('Erro', 'Preencha todos os campos do Gráfico 3:')
        return 0



def equacao_2_grau():
    if Verifica() == 1:
        
        A = float(coeficiente_a.get())
        B = float(coeficiente_b.get())
        C = float(coeficiente_c.get())

        x = np.linspace(-10, 10,100)
        y = A*x*x + B*x + C

        fig = plt.figure(figsize=(14,9), dpi=60)
        ax = fig.add_subplot(1, 1, 1)
        chart = FigureCanvasTkAgg(fig, frameLeft)
        chart.get_tk_widget().grid(row = 0, column = 0)

        plt.cla()
    
   
        ax.spines['left'].set_position('zero')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        plt.plot(x,y, 'b')
    





janela = Tk()
janela.title("Equação do Segundo Grau")
janela.geometry('1200x550')
janela.configure(background=co1, highlightbackground=co0, highlightthickness=1)
janela.resizable(width=FALSE, height=FALSE)

frameLeft =  Frame(janela, width = 850,  height = 550, bg = co1, highlightbackground=co0, highlightthickness=1)
frameLeft.place(x=0, y=0)


frameRight =  Frame(janela, width = 350,  height = 400, bg = co1, highlightbackground=co0, highlightthickness=1)
frameRight.place(x=850, y=0)


frameRightBaixo =  Frame(janela, width = 350,  height = 150, bg = co2, highlightbackground=co0, highlightthickness=1)
frameRightBaixo.place(x=850, y=400)

coef_label = Label(frameRight, text= "Entre com os valores dos coeficientes:", font=('Verdana 12 bold'),bg=co1, fg=co2)
coef_label.place(x=5, y=10)

coef_a_label = Label(frameRight, text= "A:", font=('Verdana 13 bold'),bg=co1, fg=co2)
coef_a_label.place(x=40, y=70)
coeficiente_a = Entry(frameRight, relief="solid")
coeficiente_a.place(x=65, y=65, width = 30,  height = 30)

coef_b_label = Label(frameRight, text= "B:", font=('Verdana 13 bold'),bg=co1, fg=co2)
coef_b_label.place(x=120, y=70)
coeficiente_b = Entry(frameRight, relief="solid")
coeficiente_b.place(x=145, y=65, width = 30,  height = 30)

coef_c_label = Label(frameRight, text= "C:", font=('Verdana 13 bold'),bg=co1, fg=co2)
coef_c_label.place(x=200, y=70)
coeficiente_c = Entry(frameRight, relief="solid")
coeficiente_c.place(x=225, y=65, width = 30,  height = 30)


plotar_button = Button(frameRight, command = equacao_2_grau, text="Plotar", width=25,  font=('ivy 13 bold'),bg=co2, fg=co1, overrelief=RIDGE)
plotar_button.place(x=30, y=120)


funcao_label = Label(frameRightBaixo, text="Y = AX^2  + BX +C", width= 19, height=5, font=('Verdana 19 bold'), bg=co2, fg=co1)
funcao_label.grid(row=0, column=0)
