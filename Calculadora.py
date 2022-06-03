# importação da biblioteca
from tkinter import *

'----------------------------------------------------------------------------------------------------------------------'
# comandos para os botões
def entrada(valor):
    label['text'] += valor


def saida():
    label['text'] = eval(label['text'])
    label['text'] = str(label['text'])


def limpar():
    label['text'] = ''


def deletar():
    label['text'] = label['text'][:-1]

'----------------------------------------------------------------------------------------------------------------------'
# criação da janela
janela = Tk()
janela.geometry('250x300+830+200')
janela.config(background='#62626e')

'----------------------------------------------------------------------------------------------------------------------'
# comando p/ o teclado
janela.bind('0', lambda event: entrada('0'))
janela.bind('1', lambda event: entrada('1'))
janela.bind('2', lambda event: entrada('2'))
janela.bind('3', lambda event: entrada('3'))
janela.bind('4', lambda event: entrada('4'))
janela.bind('5', lambda event: entrada('5'))
janela.bind('6', lambda event: entrada('6'))
janela.bind('7', lambda event: entrada('7'))
janela.bind('8', lambda event: entrada('8'))
janela.bind('9', lambda event: entrada('9'))
janela.bind('.', lambda event: entrada('.'))

janela.bind('-', lambda event: entrada('-'))
janela.bind('+', lambda event: entrada('+'))
janela.bind('*', lambda event: entrada('*'))
janela.bind('/', lambda event: entrada('/'))
janela.bind('(', lambda event: entrada('('))
janela.bind(')', lambda event: entrada(')'))

janela.bind('<Return>', lambda event: saida())
janela.bind('<BackSpace>', lambda event: deletar())
janela.bind('<Escape>', lambda event: limpar())

'----------------------------------------------------------------------------------------------------------------------'
# configuração das linhas e colunas
janela.grid_rowconfigure(0, weight=1)
janela.grid_rowconfigure(1, weight=1)
janela.grid_rowconfigure(2, weight=1)
janela.grid_rowconfigure(3, weight=1)
janela.grid_rowconfigure(4, weight=1)
janela.grid_rowconfigure(5, weight=1)

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)
janela.grid_columnconfigure(2, weight=1)
janela.grid_columnconfigure(3, weight=1)

'----------------------------------------------------------------------------------------------------------------------'
# criação dos widgets
label = Label(text='', font='Arial 14 bold', fg='white', bg='#62626e')

btn0 = Button(text='0', font='Arial 14 bold', width=3, command=lambda: entrada('0'))
btn1 = Button(text='1', font='Arial 14 bold', width=3, command=lambda: entrada('1'))
btn2 = Button(text='2', font='Arial 14 bold', width=3, command=lambda: entrada('2'))
btn3 = Button(text='3', font='Arial 14 bold', width=3, command=lambda: entrada('3'))
btn4 = Button(text='4', font='Arial 14 bold', width=3, command=lambda: entrada('4'))
btn5 = Button(text='5', font='Arial 14 bold', width=3, command=lambda: entrada('5'))
btn6 = Button(text='6', font='Arial 14 bold', width=3, command=lambda: entrada('6'))
btn7 = Button(text='7', font='Arial 14 bold', width=3, command=lambda: entrada('7'))
btn8 = Button(text='8', font='Arial 14 bold', width=3, command=lambda: entrada('8'))
btn9 = Button(text='9', font='Arial 14 bold', width=3, command=lambda: entrada('9'))

btnMult = Button(text='*', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: entrada('*'))
btnDiv = Button(text='/', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: entrada('/'))
btnMais = Button(text='+', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: entrada('+'))
btnSub = Button(text='-', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: entrada('-'))

btnResult = Button(text='=', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: saida())
btnLimpar = Button(text='C', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: limpar())
btnPonto = Button(text='•', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: entrada('.'))
btnDelet = Button(text='Del', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: deletar())
btnAParent = Button(text='(', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: entrada('('))
btnFParent = Button(text=')', font='Arial 14 ', width=3, bg='#e0e0e0', command=lambda: entrada(')'))

'----------------------------------------------------------------------------------------------------------------------'
# organização do widgets
label.grid(row=0, column=0, columnspan=4)

btn1.grid(row=4, column=0, sticky=NSEW)
btn2.grid(row=4, column=1, sticky=NSEW)
btn3.grid(row=4, column=2, sticky=NSEW)
btn4.grid(row=3, column=0, sticky=NSEW)
btn5.grid(row=3, column=1, sticky=NSEW)
btn6.grid(row=3, column=2, sticky=NSEW)
btn7.grid(row=2, column=0, sticky=NSEW)
btn8.grid(row=2, column=1, sticky=NSEW)
btn9.grid(row=2, column=2, sticky=NSEW)
btn0.grid(row=5, column=0, sticky=NSEW)

btnMult.grid(row=2, column=3, sticky=NSEW)
btnDiv.grid(row=3, column=3, sticky=NSEW)
btnMais.grid(row=4, column=3, sticky=NSEW)
btnSub.grid(row=5, column=3, sticky=NSEW)

btnResult.grid(row=5, column=2, sticky=NSEW)
btnLimpar.grid(row=1, column=0, sticky=NSEW)
btnPonto.grid(row=5, column=1, sticky=NSEW)
btnDelet.grid(row=1, column=3, sticky=NSEW)
btnAParent.grid(row=1, column=1, sticky=NSEW)
btnFParent.grid(row=1, column=2, sticky=NSEW)

'----------------------------------------------------------------------------------------------------------------------'
# execução
mainloop()
