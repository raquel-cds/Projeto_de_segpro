import customtkinter as ctk

# Configuração inicial da interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class JanelaBase:
    def __init__(self):
        self.window = ctk.CTk()  # Janela principal
        self.configurar_janela()

    def configurar_janela(self):
        self.window.title('Calculadora de Dispersão')
        self.window.geometry("600x680")
        self.window.resizable(width=True, height=True)
        self.window.maxsize(width=900, height=680)
        self.window.minsize(width=500, height=400)

class Aplicacao(JanelaBase):
    def __init__(self):
        super().__init__()  # Chama o construtor de JanelaBase
        self.textos()
        self.botoes()
        # Instancia o formulário e o controlador, passando o formulário para o controlador
        self.formulario = Formulario(self.window)
        self.controlador = ControladorDeCaptura(self.window, self.formulario)
        self.window.mainloop()  # Inicia o loop principal da interface

    def botoes(self):
        self.opcoes = ctk.CTkOptionMenu(self.window, values=["Puff"])
        self.opcoes.pack(pady=30, padx=30)
        self.opcoes.set("Escolha um modelo")

    def textos(self):
        self.titulo = ctk.CTkLabel(self.window, text="Seja bem-vindo(a) ao nosso aplicativo", font=("Arial Bold", 20))
        self.titulo.pack(pady=20)

        self.introducao = ctk.CTkTextbox(self.window, width=350, height=150)
        self.introducao.pack(pady=20)
        self.introducao.insert("0.0", "Explore as funcionalidades e veja como os nossos recursos podem ajudar a prever e mitigar impactos ambientais de forma precisa e eficiente.")

class Formulario:
    def __init__(self, window):
        self.window = window
        self.entradas = []  # Lista para armazenar as caixas de entrada
        self.criar_entradas()

    def criar_entradas(self):
        # Cria 6 caixas de entrada
        for i in range(6):
            entrada = ctk.CTkEntry(self.window, placeholder_text=f"Digite o valor {i + 1}...")
            entrada.pack(expand=True, fill='x', padx=50, pady=10)
            self.entradas.append(entrada)  # Armazena cada caixa de entrada na lista

    def obter_dados(self): # REFORMULAR ESTÁ PARTE COM O CÓDIGO DO MATEUS
        # Retorna uma lista com o conteúdo de cada caixa de entrada
        return [entrada.get() for entrada in self.entradas]

class ControladorDeCaptura:
    def __init__(self, window, formulario):
        self.window = window
        self.formulario = formulario
        self.mensagem_erro = None  # Label para a mensagem de erro
        self.criar_botao()

    def criar_botao(self):
        # Cria o botão "Enviar" e associa-o ao método capturar_informacoes
        self.botao = ctk.CTkButton(self.window, text="Enviar", command=self.capturar_informacoes)
        self.botao.pack(pady=20)

    def capturar_informacoes(self):
        # Obtém os dados do formulário e verifica se todas as caixas foram preenchidas
        dados = self.formulario.obter_dados()
        dados_incompletos = any(not dado for dado in dados)
        
        if dados_incompletos:
            self.exibir_erro("Por favor, preencha todas as caixas de entrada.")
        else:
            if self.mensagem_erro and self.mensagem_erro.winfo_exists():
                self.mensagem_erro.destroy()  # Oculta a mensagem de erro se já estiver exibida

            # PROCESSA OS DADOS FORNECIDOS # REFORMULAR COM O CÓDIGO DO MATEUS
            for i, dado in enumerate(dados, start=1):
                print(f"Dado {i}: {dado}")

    def exibir_erro(self, mensagem):
        # Exibe uma mensagem de erro em uma janela modal
        if not (self.mensagem_erro and self.mensagem_erro.winfo_exists()):  # Evita múltiplas janelas de erro
            self.mensagem_erro = ctk.CTkToplevel(self.window)
            self.mensagem_erro.title("Erro")
            self.mensagem_erro.geometry("400x150")
            # impedindo que o usuário interaja com a janela principal até que feche a janela de erro.
            self.mensagem_erro.transient(self.window)  # Mantém a janela de erro em primeiro plano
            self.mensagem_erro.grab_set()  # Torna a janela modal

            label_erro = ctk.CTkLabel(self.mensagem_erro, text=mensagem, text_color="red") # Abre uma nova janela
            label_erro.pack(pady=20)
            botao_ok = ctk.CTkButton(self.mensagem_erro, text="OK", command=self.mensagem_erro.destroy)
            botao_ok.pack(pady=10)

# Inicia a aplicação
Aplicacao()



# TO DO -------------------------------------------------------------------------------------

# criar classes só para capturar as informações - formulário (EM ANDAMENTO) (ok)
# se estiver faltando alguma informações, impedir que o botão retorne algo (EM ANDAMENTO) (ok)
# 1 botão de enviar somente! (EM ANDAMENTO) (ok)
# criar caixas de dialogo que salve as informações do usuário (ok)

# reformular tamanho 
# criar janela só para os inputs das informações
# janela - resultado (Botão enviar retornando uma janela com os resultados) (EM ANDAMENTO)
# Entry
# adicionar funcionalidade as botões/caixa de entrada (retornar algo) - if else (??)
# fazer botão ENTER funcionar
# informações retornadas aparecerem na tela
# criar janela de apresentação
# fazer a responsividade não comer os botoes
# CtkOptionMenu não suporta text