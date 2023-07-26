import customtkinter

# usar o comando pip install customtkinter para intalar o bibloteca no cmd 


janela = customtkinter.CTk()
janela.geometry("500x300")  

def clique():  
    print("Fazer login")

texto = customtkinter.CTkLabel(janela,text="Fazer Login")
texto.pack(padx=10, pady=10)  

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10 )

janela.mainloop()

