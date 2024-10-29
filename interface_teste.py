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
        self.informacoes = Informacoes() # ERRO
        self.window.mainloop() # exibe a janela com a ajuda do loop
        

    def tela(self): 
        self.window.title('Calculadora de Dispersão') # Definindo título da janela
        self.window.geometry("600x680") # dimensões que minha janela irá iniciar
        self.window.resizable(width=True, height=True) # responsividade da tela
        self.window.maxsize(width=900, height=680)
        self.window.minsize(width=500, height=400)
    
    def botoes(self):
        self.opcoes = ctk.CTkOptionMenu(self.window, values=["Pluma", "Puff"]) # valores são armazenados dentro de uma lista
        self.opcoes.pack(pady=30, padx=30)
        self.opcoes.set("Escolha um modelo") # adiciona um título ao botão

    def textos(self):
        self.titulo = ctk.CTkLabel(self.window, text="Seja bem-vindo(a) ao nosso aplicativo", font=("arial bold", 20))
        self.titulo.pack(pady=20)

        self.introducao = ctk.CTkTextbox(self.window, width=350, height=150)
        self.introducao.pack(pady=20)
        self.introducao.insert("0.0", "Explore as funcionalidades e veja como os nossos recursos podem ajudar a prever e mitigar impactos ambientais de forma precisa e eficiente.")


class Informacoes():
    def __init__(self):
        self.informacoes()
        self.botao_capturar()

    def capturar_informacoes(self): # INTERNO AO BOTÃO_CAPTURAR / IRÁ RETORNAR AS INFORMAÇÕES
        ''' if # todas as entradas foram preenchidas, faça: '''
        print(f"BOTÃO RETORNANDO!")
        print(f'DADOS A')
        print(f'DADOS B')
        print(f'DADOS C')

    def botao_capturar(self):
        self.botao = ctk.CTkButton(self.window, text="Enviar", command=self.capturar_informacoes) # vai retorar a função capturar_informações
        self.botao.pack(pady=20)
    
    def informacoes(self):
        self.entrada = ctk.CTkEntry(self.window, placeholder_text="Digite algo aqui...")
        self.entrada.pack(expand=True, fill='x', padx=50, pady=20) # padx e pady são as margem da minha caixa
        self.entrada2 = ctk.CTkEntry(self.window, placeholder_text="Digite algo aqui...").pack(pady=20)

Aplicacao()

# TO DO -------------------------------------------------------------------------------------

# criar classes só para as informações (EM ANDAMENTO)
# janela - resultado (Botão enviar retornando uma janela com os resultados) (EM ANDAMENTO)
# 1 botão de enviar somente! (EM ANDAMENTO)
# se estiver faltando alguma informações, impedir que o botão retorne algo (EM ANDAMENTO)

# Entry
# criara caixas de dialogo que salve as informações do usuário
# adicionar funcionalidade as botões/caixa de entrada (retornar algo) - if else (??)
# fazer botão ENTER funcionar
# informações retornadas aparecerem na tela
# criar janela de apresentação
# criar janela só para os inputs das informações
# fazer a responsividade não comer os botoes


# CtkOptionMenu não suporta text