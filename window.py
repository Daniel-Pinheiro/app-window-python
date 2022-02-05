from tkinter import *

def func():
    textoResposta['text'] = campoTexto.get()
    campoTexto.delete(0,END)

janela = Tk()
janela.title("Simples aplicativo de janela")
# janela.configure(background='#fff')

texto = Label(janela, text="Clique no botão pra carregar texto do campo:")
texto.grid(column=0, row=0, padx=10, pady=10)

campoTexto = Entry(janela, width=30, )
campoTexto.grid(column=0, row=1, padx=10, pady=10)

textoResposta = Label(janela, text="")
textoResposta.grid(column=0, row=2, padx=10, pady=10)

botao = Button(janela, text="Atualiza", command=func)
botao.grid(column=0, row=3, padx=10, pady=10)

janela.mainloop()