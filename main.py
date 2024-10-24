from math import exp, pow, pi, sqrt
#import numpy as np

class Puff():
    def __init__(self, hr, tipo_atm, v_vento):
        
        self.hr = hr            # Dado em metros (m). hr = altura valvula + altura tunel        
        self.tipo_atm = tipo_atm     # Por conveniência
        self.v_vento = v_vento          # Dado em metros/segundo (m/s) 
        self.periodo = 0        # 0 = dia. Até expandirmos a calculadora


    # Valores de sigma
    def sigma_puff(self, atm, dist):
        '''
        Retorna os coeficientes de dispersão para PUFF.
        
        Argumentos:
        atm     - condições da atmosfera, string A, B, C, D, E ou F (procure referência)
        dist    - distância horizontal entre a fonte e o ponto de interesse na direção do vento (m), float
        '''
        
        self.tipo_atm = atm

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
    
    
    # Equações para o efeito PUFF

    def pasquill_gifford_15(self, qm, posicao, t):
        '''
        Modelo de Pasquill-Gifford para dispersão (origem das coordenadas abaixo da fonte, no solo).
        Retorna a concentração média de uma substancia num certo ponto do espaço.
        
        Argumentos:
        qm      - vasão máxima (kg/s), float
        posicao - posição a ser analisada (m), tupla (x, y, z) de float
        t       - tempo depois da liberação do puff (s), float
        '''

        x, y, z = posicao
        dist = sqrt(pow(x, 2) + pow(y, 2) + pow((z - self.hr), 2)) # Distancia entre a fonte e o local analisado
        

        sigx, sigy, sigz = self.sigma_puff(self.tipo_atm, dist)

        exp_y = exp((-pow(y / sigy , 2) / 2))
        exp_z = exp(-pow((z - self.hr) / sigz, 2) / 2) + exp(-pow((z + self.hr) / sigz, 2) / 2)
        exp_xut = exp(-pow((x - self.v_vento * t) / sigx, 2) / 2)
        sub = (pow((2*pi), 3/2)) * sigx * sigy * sigz

        concent = (qm * exp_y * exp_z * exp_xut) / sub

        return concent



# Em construção -----------------------------------------------------------------

def tempo_exposicao(x, y, z = 0):
    # Gráfico (f = concentração num ponto)x(t = tempo)
    # Tomo t1 como o primeiro t com f > 0, e t2 como o próximo t com f = 0
    # t2-t1 = tempo de exposição do usuário que permanece parado numa posição
    return


# toxicidade (toxicologia ocupacional)

def toxicidade_CL50(self, subst, tempo_expo):
    # conta relacionando tempo de exposição e concentração do elemento

    tox_subs = {'Extrema': ['ozônio', 'isocianato de metila'],
                'Alta': ['fosgênio', 'dióxido de nitrogênio'],
                'Moderada': ['ácido cianídrico', 'dióxido de enxofre'],
                'Baixa': ['amônia'],
                'Muito baixa': ['tolueno'],
                'Relativamente atóxica': ['fluorcarbonos']}
    return
