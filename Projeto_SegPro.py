import numpy as np
import matplotlib.pyplot as plt
from os import system

x = np.arange(1, 5000, 10)
y = np.arange(-500, 500, 0.5)
X, Y = np.meshgrid(x, y) #cria a grade de valores xy em z
z = 1

wind = float(input("Qual é a velocidade do vento, em m/s?\n"))
insol = str(input("Qual é o nivel de incidencia solar, Alto ou Baixo?\n")).capitalize()
Qtm = int(input("Quanto material foi expelido, em kg?\n"))
Qtm*=1000
dist = float(input("Qual a sua distância, em uma linha reta em metros, da fonte de emissão?\n"))
deg_puff = float(input("Qual a direção aproximada da fonte de emissão, em graus?\n"))
deg_wind = str(input("Qual a direção cardeal do vento?(N, NE, E, SE, S, SO, O, NO)\n")).capitalize()
t = 0

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
if rad >= np.pi/2 and dist > 50:
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
ax.set_zlabel('Concentração')
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
    ax.set_zlabel('Concentração')
    ax.set_title(f"Concentração com base no centro de emissão\n por segundos t = {t}")
    ax.scatter(x_pos, y_pos, 1, c = "red")

    plt.pause(0.5) 


plt.show()
system('cls')
