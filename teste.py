import customtkinter as ctk

# usar o comando pip install customtkinter para intalar o bibloteca no cmd 

def show_message_box(title, message):
    top = ctk.CTk()
    top.geometry("300x150")
    top.title(title)

    text_label = ctk.CTkLabel(top, text=message)
    text_label.pack(padx=20, pady=20)

    ok_button = ctk.CTkButton(top, text="OK", command=top.destroy,fg_color="#8A2BE2")
    ok_button.pack(pady=10)

    top.mainloop()

def clique():
    nome = nome_entry.get()
    login = login_entry.get()
    senha = senha_entry.get()

    if nome and login and senha:
        print("Fazer login")

        with open("teste.txt", "a") as arquivo:
            arquivo.write(f"Nome do usuário: {nome},  login: {login}, senha: {senha}\n")

        # Exibir mensagem de usuário cadastrado
        show_message_box("Sucesso!", "Usuário cadastrado com sucesso!")
    else:
        print("Por favor, preencha todos os campos!")

janela = ctk.CTk()
janela.geometry("500x300") 
ctk.set_appearance_mode("dark")

texto = ctk.CTkLabel(janela, text="Cadastrar conta")
texto.pack(padx=10, pady=10)

nome_entry = ctk.CTkEntry(janela, placeholder_text="Nome do usuário ")
nome_entry.pack(padx=10, pady=10)

login_entry = ctk.CTkEntry(janela, placeholder_text="Crie seu login")
login_entry.pack(padx=10, pady=10)

senha_entry = ctk.CTkEntry(janela, placeholder_text="Crie sua senha", show="*")
senha_entry.pack(padx=10, pady=10)

botao = ctk.CTkButton(janela, text="cadastrar", command=clique, fg_color="#8A2BE2")
botao.pack(padx=10, pady=10)

janela.mainloop()
