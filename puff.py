from math import exp, pow, pi, sqrt
import numpy as np


# Função distância
def distancia(hr, x, y, z):
    '''
    Retorna a distância euclidiana entre a fonte e algum ponto do espaço, não podendo ser zero.
    
    Argumentos:
    x, y, z     - float, float, float (m).
    '''
    dist = sqrt(pow(x, 2) + pow(y, 2) + pow((z - hr), 2)) # Distancia entre a fonte e o local analisado

    if dist == 0:
        print('A distância não pode ser zero. Tente outras coordenadas.')
        return
    
    else:
        return dist
    

# Valores de sigma
# Fazer tratamento de erro: divisão por zero
def sigma_puff(atm, dist = 1):
    '''
    Retorna os coeficientes de dispersão para um PUFF(admensionais), dado um tipo de atmosfera, num ponto à uma certa distância.
    
    Argumentos:
    atm     - string A, B, C, D, E ou F (procure referência), condições da atmosfera.
    dist    - float (m), distância horizontal entre a fonte e o ponto de interesse na direção do vento.
    '''

    if atm == 'A':
        sigxy = 0.18 * pow(dist, 0.92)
        sigz = 0.60 * pow(dist, 0.75)

    elif atm == 'B':
        sigxy = 0.14 * pow(dist, 0.92)
        sigz = 0.53 * pow(dist, 0.73)

    elif atm == 'C':
        sigxy = 0.10 * pow(dist, 0.92)
        sigz =  0.34 * pow(dist, 0.71)

    elif atm == 'D':
        sigxy = 0.06 * pow(dist, 0.92)
        sigz =  0.15 * pow(dist, 0.70)

    elif atm == 'E':
        sigxy = 0.04 * pow(dist, 0.92)
        sigz =  0.10 * pow(dist, 0.65)

    elif atm == 'F':
        sigxy = 0.02 * pow(dist, 0.89)
        sigz =  0.05 * pow(dist, 0.61)

    return sigxy, sigxy, sigz


# Equações para o efeito PUFF caso 15

class Puff():
    def __init__(self, atm, hr, u, qm):
        self.atm = atm
        self.hr = hr
        self.u = u
        self.qm = qm

    # !!! Arrumar conforme os parâmetros da classe
    def pasquill_gifford_15(self, x, y, z, t):
        '''
        Modelo de Pasquill-Gifford para dispersão (origem das coordenadas abaixo da fonte, no solo).
        Retorna a concentração média (float, kg/m³) de um poluente num ponto (x,y,z) depois de t segundos.
        
        Argumentos:
        x, y, z - float, float, float (m), posição a ser analisada.
        t       - float (s), tempo depois da liberação do puff.
        '''

        dist = distancia(x, y, z) # Distancia entre a fonte e o local analisado

        sigx, sigy, sigz = sigma_puff(self.atm, dist)

        exp_y = exp((-pow(y / sigy , 2) / 2))
        exp_z = exp(-pow((z - self.hr) / sigz, 2) / 2) + exp(-pow((z + self.hr) / sigz, 2) / 2)
        exp_xut = exp(-pow((x - self.u * t) / sigx, 2) / 2)
        sub = (pow((2*pi), 3/2)) * sigx * sigy * sigz

        concent = (self.qm * exp_y * exp_z * exp_xut) / sub

        return concent
    
            # Em construção -----------------------------------------------------------------
    def area_segura(self, x, y, z = 0):
        t_axis = np.arange(0, 1000, 1)
        x_aixs = np.arange(-5000, 5000, 100)

        for i in t_axis:
            c = np.array(pasquill_gifford_15(x, 0, self.hr, i))
        
        
        
        y_axis = np.array()

        return




def tempo_exposicao(x, y, z = 0):
    # Gráfico (f = concentração num ponto)x(t = tempo)
    # Tomo t1 como o primeiro t com f > 0, e t2 como o próximo t com f = 0
    # t2-t1 = tempo de exposição do usuário que permanece parado numa posição
    
    
    return


# toxicidade (toxicologia ocupacional)

def toxicidade_CL50(subst, tempo_expo):
    # conta relacionando tempo de exposição e concentração do elemento

    tox_subs = {'Extrema': ['ozônio', 'isocianato de metila'],
                'Alta': ['fosgênio', 'dióxido de nitrogênio'],
                'Moderada': ['ácido cianídrico', 'dióxido de enxofre'],
                'Baixa': ['amônia'],
                'Muito baixa': ['tolueno'],
                'Relativamente atóxica': ['fluorcarbonos']}
    return



if __name__ == '__main__':

    print('oi')