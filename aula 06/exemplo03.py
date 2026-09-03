# Exercício 1: Calculadora de Idade com Interface Gráfica

import tkinter as tk
from tkinter import messagebox
import os

os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'

# Desenvolver uma aplicação desktop em Python utilizando a biblioteca Tkinter que receba o ano
# de nascimento de uma pessoa e apresente a idade correspondente com base no ano atual.

def calc_idade():
    birth = entry_birth.get()
    current_year = entry_current_year.get()
    if birth and current_year:
        age = int(current_year) - int(birth)
        messagebox.showinfo("Dados recebidos", f'iade é {age}')



janela = tk.Tk()
janela.title = ('Calculadora de idade')
janela.geometry('400x300')

# entra o ano que nasceu

label_birth = tk.Label(janela, text='Digite o ano que nasceu')
label_birth.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_birth = tk.Entry(janela, width=30)
entry_birth.grid(row=0, column=1, padx=10, pady=10)

# entra o ano atual
label_current_year = tk.Label(janela, text='Digite o ano atual')
label_current_year.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_current_year = tk.Entry(janela, width=30)
entry_current_year.grid(row=1, column=1, padx=10, pady=10)

botao_cadastrar = tk.Button(janela, text="Enviar", command=calc_idade)
botao_cadastrar.grid(row=2, column=0, columnspan=2, pady=20) # columnspan=2 faz o botão ocupar 2 colunas

janela.mainloop()

# calc_idade()