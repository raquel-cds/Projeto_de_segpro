import customtkinter as ctk

janela = ctk.CTk()
ctk.set_appearance_mode("dark")  # Define o modo escuro (dark, light ou system)
ctk.set_default_color_theme("blue")  # Define o tema de cor

class Aplicacao():
    def __init__(self):
        self.window = janela
        self.tela()
        self.botoes()
        self.window.mainloop() # exibe a janela com a ajuda do loop

    def tela(self): 
        self.window.title('Calculadora de Dispersão') # Definindo título da janela
        self.window.geometry("600x680") # dimensões que minha janela irá iniciar
        self.window.resizable(width=True, height=True) # responsividade da tela
        self.window.maxsize(width=900, height=680)
        self.window.minsize(width=500, height=400)
    
    def botoes(self):
        self.botaomultiplo = ctk.CTkButton(self.window, text="Escolha um modelo", fg_color="green", hover_color="lightgreen")
        self.botaomultiplo.pack(pady=30)
        self.opcao = ctk.CTkButton(self.window, text="Escolha uma opção")
        self.opcao.pack()


Aplicacao()