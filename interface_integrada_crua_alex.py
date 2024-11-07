import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from os import system

system('cls')

class Aplicacao:
    def __init__(self):
        self.window = ctk.CTk()  # Janela principal
        self.window.title("Aplicação de Entradas")
        self.window.geometry("600x400")
        
        self.entradas = []  # Lista para armazenar as entradas
        self.valores = []   # Lista para armazenar os valores dos campos
        
        self.criar_entradas()
        self.criar_botao()

        self.window.mainloop()

    def criar_entradas(self):
        """Cria 6 campos de entrada e os adiciona na lista de entradas"""

        entrada_wind = ctk.CTkEntry(self.window, placeholder_text=f"Velocidade do Vento em [m/s]")
        entrada_wind.pack(pady=10, padx=50, fill="x")
        self.entradas.append(entrada_wind)  # Armazenando cada entrada na lista

        entrada_insol = ctk.CTkEntry(self.window, placeholder_text=f"Nível de Incidência Solar (Alto / Baixo)")
        entrada_insol.pack(pady=10, padx=50, fill="x")
        self.entradas.append(entrada_insol)  

        entrada_Qtm = ctk.CTkEntry(self.window, placeholder_text=f"Quantidade de material expelido em [Kg]")
        entrada_Qtm.pack(pady=10, padx=50, fill="x")
        self.entradas.append(entrada_Qtm)

        entrada_dist = ctk.CTkEntry(self.window, placeholder_text=f"Distância Linear da Fonte de Emissão em [m]")
        entrada_dist.pack(pady=10, padx=50, fill="x")
        self.entradas.append(entrada_dist)

        entrada_deg_puff = ctk.CTkEntry(self.window, placeholder_text=f"Direção aproximada da Fonte de Emissão em graus")
        entrada_deg_puff.pack(pady=10, padx=50, fill="x")
        self.entradas.append(entrada_deg_puff)

        entrada_deg_wind = ctk.CTkEntry(self.window, placeholder_text=f"Direção Cardeal do Vento(N, NE, E, SE, S, SO, O, NO)")
        entrada_deg_wind.pack(pady=10, padx=50, fill="x")
        self.entradas.append(entrada_deg_wind)

    def criar_botao(self):
        """Cria o botão 'Enviar' que irá capturar os dados inseridos"""
        botao = ctk.CTkButton(self.window, text="Enviar", command=self.obter_dados)
        botao.pack(pady=20)

    def obter_dados(self):
        """Obtém os dados inseridos nas caixas de entrada"""
        self.valores = [entrada.get() for entrada in self.entradas]  # Captura os valores das entradas
        self.mostrar_dados()  # Exibe os dados no console para fins de demonstração

    def mostrar_dados(self):
        """Exibe os dados no console"""
        for i, valor in enumerate(self.valores, start=1):
            print(f"Valor {i}: {valor}")
        self.window.destroy()

    def obter_valor(self, indice):
        """Retorna o valor de um campo específico com base no índice"""
        if indice in (0, 2, 3, 4):
            return float(self.valores[indice])  # Converte o valor para float para operações matemáticas
        if indice in (1, 5):
            return str(self.valores[indice])  # Converte o valor para str
        return None
# Iniciar a aplicação
Apl = Aplicacao()


wind = Apl.obter_valor(0)
insol = Apl.obter_valor(1)
Qtm = Apl.obter_valor(2)
dist = Apl.obter_valor(3)
deg_puff = Apl.obter_valor(4)
deg_wind = Apl.obter_valor(5)
t = 0


"----------------------------Fim da Interface----------------------------"

x = np.arange(1, 5000, 10)
y = np.arange(-500, 500, 0.5)
X, Y = np.meshgrid(x, y) #cria a grade de valores xy em z
z = 1


# transforma a direção do vento e adireção da fonte de emissão em radianos
rad_puff = (deg_puff*np.pi)/180
if deg_wind == "N":
    rad_wind = 0
elif deg_wind == "Ne":
    rad_wind = np.pi/4
elif deg_wind == "E":
    rad_wind = np.pi/2
elif deg_wind == "Se":
    rad_wind = 3*np.pi/4
elif deg_wind == "S":
    rad_wind = np.pi
elif deg_wind == "So":
    rad_wind = 5*np.pi/4
elif deg_wind == "O":
    rad_wind = 3*np.pi/2
elif deg_wind == "No":
    rad_wind = 7*np.pi/4

# angulo entre o o vento e distancia à fonte de emissão relativo à um observador
rad = np.absolute(rad_puff - rad_wind)

# posição relativa do observador
x_pos = dist*np.cos(rad)
y_pos = dist*np.sin(rad)
z_pos = 0
if (rad >= np.pi/2) and (dist > 50):
    print("Você está completamente seguro desta emissão!")


sig_y = sig_z = sig_x = 1 # sig são as dispersões da poluição em X, y e z

Hr = 5 # altura do puff
u = wind # velocidade do vento no eixo-X

# função que liga a velocidade do vento e nível de incidencia solar
# à uma classe de estabilidade atmosférica específica
match wind:
    case wind if wind <= 2:
        if insol == "Baixo":
            stabc = "B"
        else: stabc = "A"
    case wind if 2 < wind <= 3:
        if insol == "Baixo":
            stabc = "C"
        else: stabc = "B"
    case wind if 3 < wind <= 4:
        if insol == "Baixo":
            stabc = "C"
        else: stabc = "B"
    case wind if 4 < wind <= 6:
        if insol == "Baixo":
            stabc = "D"
        else: stabc = "C"
    case wind if wind > 6:
        if insol == "Baixo":
            stabc = "D"
        else: stabc = "C"

# stac é a classe de estabilidade atmosférica que determina os sigmas
if stabc == "A":
    sig_y = sig_x = 0.18*np.power(X, 0.92)
    sig_z = 0.6 * np.power(X, 0.75)
elif stabc == "B":
    sig_y = sig_x = 0.14*np.power(X, 0.92)
    sig_z = 0.53*np.power(X, 0.73)
elif stabc == "C":
    sig_y = sig_x = 0.1*np.power(X, 0.92)
    sig_z = 0.34*np.power(X, 0.71)
elif stabc == "D":
    sig_y = sig_x = 0.06*np.power(X, 0.92)
    sig_z = 0.15*np.power(X, 0.7)


#Equação do caso 15
Z = (Qtm/(((2*np.pi)**3/2)*sig_x*sig_y*sig_z))*(np.e**(-0.5*((Y/sig_y)**2)))*\
    ((np.e**(-0.5*((z-Hr)/sig_z)**2))+(np.e**(-0.5*((z+Hr)/sig_z)**2)))*(np.e**\
    (-0.5*((X-u*t)/sig_x)**2))

# Gráfico
fig = plt.figure()
ax = plt.axes()
ax.contourf(X, Y, Z, cmap='inferno')
ax.set_xlabel('Distância(m)')
ax.set_ylabel('Amplitude do Puff(m)')
ax.scatter(x_pos, y_pos, 1)

# Animação do gráfico para t de 0 à 1 hora
for i in range(120):
    t+=30
    Z = (Qtm/(((2*np.pi)**3/2)*sig_x*sig_y*sig_z))*(np.e**(-0.5*((Y/sig_y)**2)))*\
        ((np.e**(-0.5*((z-Hr)/sig_z)**2))+(np.e**(-0.5*((z+Hr)/sig_z)**2)))*(np.e**\
        (-0.5*((X-u*t)/sig_x)**2))
    ax.clear()
    ax.contourf(X, Y, Z, cmap='inferno')
    ax.set_xlabel('Distância(m)')
    ax.set_ylabel('Amplitude da emissão(m)')
    ax.set_title(f"Concentração com base no centro de emissão\n por minutos t = {t/60}")
    ax.scatter(x_pos, y_pos, c = "white")

    plt.pause(0.5) 


plt.show()
system('cls') #limpa os inputs do terminal
