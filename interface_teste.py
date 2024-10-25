import customtkinter as ctk

janela = ctk.CTk()
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")  # Define o tema de cor

class Aplicacao():
    def __init__(self):
        self.window = janela
        self.tela()
        self.textos()
        self.botoes()
        self.window.mainloop() # exibe a janela com a ajuda do loop

    def tela(self): 
        self.window.title('Calculadora de Dispersão') # Definindo título da janela
        self.window.geometry("600x680") # dimensões que minha janela irá iniciar
        self.window.resizable(width=True, height=True) # responsividade da tela
        self.window.maxsize(width=900, height=680)
        self.window.minsize(width=500, height=400)
    
    def botoes(self):
        self.opcoes = ctk.CTkOptionMenu(self.window, values=["Pluma", "B"]) # valores são armazenados dentro de uma lista
        self.opcoes.pack(pady=30, padx=30)
        self.opcoes.set("Escolha um modelo") # adiciona um título ao botão

    def textos(self):
        self.titulo = ctk.CTkLabel(self.window, text="Seja bem-vindo(a) ao nosso site!", font=("arial bold", 20))
        self.titulo.pack(pady=20)

        self.introducao = ctk.CTkTextbox(self.window, width=350, height=150)
        self.introducao.pack(pady=20)
        self.introducao.insert("0.0", "Explore as funcionalidades e veja como os nossos recursos podem ajudar a prever e mitigar impactos ambientais de forma precisa e eficiente.")


Aplicacao()

# CtkOptionMenu não suporta text