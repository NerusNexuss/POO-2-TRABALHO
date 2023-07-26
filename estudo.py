import tkinter as tk
from tkinter import messagebox

# Cria a janela principal
janela = tk.Tk()
janela.title("Cadastro de Usuário")

# resolução da janela
largura = 800
altura = 600
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela - largura) // 2
y = (altura_tela - altura) // 2
janela.geometry(f"{largura}x{altura}+{x}+{y}")

# Função para salvar os dados do usuário
def salvar_usuario():
    nome = entry_nome.get()
    login = entry_login.get() 
    senha = entry_senha.get()

    # Aqui você pode adicionar a lógica para salvar os dados do usuário em algum lugar (por exemplo, em um arquivo ou banco de dados).


    # Exemplo: Salvando os dados em um arquivo de texto
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"Nome do usuário: {nome},  login: {login}, senha: {senha}\n")

    # Mostra uma mensagem de sucesso
    messagebox.showinfo("Cadastro", "Usuário cadastrado com sucesso!")

# Cria um frame para agrupar os elementos
frame = tk.Frame(janela)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centraliza o frame na tela

# interface com fonte 
fonte = ("Arial", 16)

# Labels usando grid
label_nome = tk.Label(frame, text="Nomo do usuário :", font=fonte)
label_nome.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)  # sticky=tk.E alinha o label à direita 

label_login = tk.Label(frame, text="Login:", font=fonte)
label_login.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5) 

label_senha = tk.Label(frame, text="senha:", font=fonte)
label_senha.grid(row=2, column=0, sticky=tk.E, padx=5, pady=5)  

#onde o usuario vai digitar
entry_nome = tk.Entry(frame, font=fonte)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

entry_login = tk.Entry(frame, font=fonte)
entry_login.grid(row=1, column=1, padx=5, pady=5) 

entry_senha = tk.Entry(frame, font=fonte)
entry_senha.grid(row=2, column=1, padx=5, pady=5)

# Botão Salvar/cadastrar usando grid
botao_salvar = tk.Button(frame, text="Cadastrar", command=salvar_usuario, font=fonte)
botao_salvar.grid(row=3, column=1,padx=10, pady=20)

# Executa a interface gráfica
janela.mainloop()
