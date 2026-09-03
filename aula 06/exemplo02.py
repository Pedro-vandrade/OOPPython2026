import tkinter as tk
from tkinter import messagebox # Importa o módulo messagebox para exibir mensagens pop-up
import os

# Define os caminhos onde o Tcl/Tk realmente reside no Python para Windows
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'



def cadastrar_usuario(): #Função chamada quando o botão 'Cadastrar' é clicado.Obtém os valores dos campos de
#usuário e senha e exibe uma mensagem
    usuario = entry_usuario.get() # Obtém o texto do campo de usuário
    senha = entry_senha.get()     # Obtém o texto do campo de senha
    if usuario and senha: # Verifica se os campos não estão vazios
        messagebox.showinfo("Cadastro Realizado", f"Usuário: {usuario}\nSenha: {senha}")
# Limpa os campos após o cadastro (opcional)
        entry_usuario.delete(0, tk.END) # Limpa do início ao fim
        entry_senha.delete(0, tk.END)
    else:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos!")


# 1. Cria a janela principal
janela = tk.Tk()
janela.title("Formulário de Cadastro")
janela.geometry("350x200") # Tamanho da janela
# --- Widgets do Formulário --
# Label e Entry para o Usuário
label_usuario = tk.Label(janela, text="Usuário:")
label_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="w") # sticky="w" alinha à esquerda
entry_usuario = tk.Entry(janela, width=30)
entry_usuario.grid(row=0, column=1, padx=10, pady=10)

# Label e Entry para a Senha
label_senha = tk.Label(janela, text="Senha:")
label_senha.grid(row=1, column=0, padx=10, pady=10, sticky="w")
entry_senha = tk.Entry(janela, show="*", width=30) # show="*" oculta a senha
entry_senha.grid(row=1, column=1, padx=10, pady=10)
# Botão de Cadastro
botao_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar_usuario)
botao_cadastrar.grid(row=2, column=0, columnspan=2, pady=20) # columnspan=2 faz o botão ocupar 2 colunas
# 3. Inicia o loop principal da aplicação
janela.mainloop()