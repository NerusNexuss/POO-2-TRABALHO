import customtkinter

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")

# def button_function():
#     print("button pressed")

# # Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# # app.mainloop()  
janela = customtkinter.CTk()
janela.geometry("500x300")  

def clique():  
    print("Fazer login")

texto = customtkinter.CTkLabel(janela,text="Fazer Login")
texto.pack(padx=10, pady=10)  

botao = customtkinter.CTkButton(janela, text="Login", command=clique)
botao.pack(padx=10, pady=10 )

janela.mainloop()

