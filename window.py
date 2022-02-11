from tkinter import *
from tkinter import ttk

janela = Tk()
janela.title("Simples aplicativo de janela")
# janela.configure(background='#fff')

sec1 = Frame(janela)
sec1.grid(row=0)

texto = Label(sec1, text="Clique no botão p/ alterar o texto do campo:")
texto.grid(row=0, padx=10, pady=10)

campoTexto = Entry(sec1, width=40)
campoTexto.grid(row=1, padx=10, pady=10)


sec3 = Frame(janela, relief='sunken', borderwidth=1)
sec3.grid(row=2, pady=10)

textoResposta = Label(sec3, text="", width=30)
textoResposta.grid(padx=10, pady=10)


sec2 = Frame(janela)
sec2.grid(row=1, sticky='w')

texto = Label(sec2, text="Ação:")
texto.grid(column=0, row=0, sticky='e', padx=10, pady=10)

opts=['Atualizar','Tornar maiúsculas', 'Tornar minúsculas', 'Inverter ordem']
caixaLista = ttk.Combobox(sec2, width=16, values=opts)
caixaLista.set('Atualizar')
caixaLista.grid(column=1, row=0, sticky='w', padx=10, pady=10)

def func():
    if caixaLista.get() == 'Atualizar':
        textoResposta['text'] = campoTexto.get()
        campoTexto.delete(0,END)

    if caixaLista.get() == 'Tornar maiúsculas':
        textoResposta['text'] = textoResposta['text'].upper()

    if caixaLista.get() == 'Tornar minúsculas':
        textoResposta['text'] = textoResposta['text'].lower()

    if caixaLista.get() == 'Inverter ordem':
        textoResposta['text'] = textoResposta['text'][::-1]

botao = Button(sec2, text="Executar", command=func)
botao.grid(column=2, row=0, padx=10, pady=10)

janela.mainloop()