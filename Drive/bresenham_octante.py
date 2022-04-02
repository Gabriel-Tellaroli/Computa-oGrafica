'''
Novamente através de dois pontos: P1 (ponto central), P2 (ponto pertencente a circunf)
Baseia-se na propriedade simétrica da circ. desta vez calculando o ponto de 1 octante; os outros são calc por sim.

Dessa vez o ângulo t deve variar de 0 a pi/4 (90 graus): para cada ponto são gerados 7 pontos de simetria

**Diminui ainda + a quantidade de cálculos trigonométricos; embora ainda utilize um pouco e a densidade dos pontos
tb varia com o raio.
'''
'''
DISPOSIÇÃO DOS OCTANTES:

            OcIII  (-y , x)          |       OcII  (y , x)
    OcIV  (-x , y)                   |                OcI  (x , y)
    _________________________________|________________________________
                                     |
    OcV  (-x , -y)                   |                OcVIII  (x , -y)
            OcVI  (-y , -x)          |       OcVII  (y , -x)
                                     |
'''

'''
ALG:

raio=√(x1−x2)²+(y1−y2)²
delta_t = pi / 180
para t = 0 até pi / 4 com passo delta_t
    x = arredonda(raio · cos(t))
    y = arredonda(raio · sen(t))
    ligue(x+x1, y+y1)
    ligue(-x+x1, y+y1)
    ligue(-x+x1, -y+y1)
    ligue(x+x1, -y+y1)
    ligue(y+x1, x+y1)
    ligue(y+x1,-x+y1)
    ligue(-y+x1,-x+y1)
    ligue(-y+x1,x+y1)
próximo t
'''

import pyglet
import math

#coordenadas iniciais da reta
p1 = [50,50]
p2 = [55,50]

raio = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2)) #raio=√(x1−x2)²+(y1−y2)²

circ = []
count = 0

x = 0
y = round(raio)

# Auxiliares de resultado ( Tella )
n_interacoes = 3
mult_dezeseis = 0

while y >= 0:
    #gera 8 pontos por iteração
    # essa parte é a referente ao alg simetria por octante
    circ.append(p1[0] + x)
    circ.append(p1[1] + y)
    circ.append(p1[0] + x)
    circ.append(p1[1] - y)
    circ.append(p1[0] - x)
    circ.append(p1[1] + y)
    circ.append(p1[0] - x)
    circ.append(p1[1] - y)

    #se retirar daqui até o último "circ.append(...)", estaremos deixando apenas o bresenham
    circ.append(p1[1] + y)
    circ.append(p1[0] + x)
    circ.append(p1[1] + y)
    circ.append(p1[0] - x)
    circ.append(p1[1] - y)
    circ.append(p1[0] + x)
    circ.append(p1[1] - y)
    circ.append(p1[0] - x)
    # fim da parte de simetria por octante

    delta_i = (x+1)**2 + (y-1)**2 - raio ** 2
    md = abs(delta_i)

    if delta_i < 0: #ponto no interior do círculo
        mh = abs((x+1)**2 + (y-1)**2 - raio**2)
        sigma = mh - md
        if sigma <= 0:
            x += 1
        else:
            x += 1
            y -= 1
    elif delta_i > 0:   #ponto fora do círculo
        mv = abs((x**2) + (y-1)**2 - raio**2)
        sigma = mv - md
        if sigma >= 0:
            x += 1
            y -= 1
        else:
            y -= 1
    else:
        x += 1
        y -= 1

    count += 1
    # Edição para visualizar os pontos das *n_interacoes*
    if count <= n_interacoes:
        print('------------------------------------')
        print('Iteracao:',count)
        print(
            '[',circ[0 + mult_dezeseis], circ[1 + mult_dezeseis],']', 
            '[',circ[2 + mult_dezeseis], circ[3 + mult_dezeseis],']', 
            '[',circ[4 + mult_dezeseis], circ[5 + mult_dezeseis],']', 
            '[',circ[6 + mult_dezeseis], circ[7 + mult_dezeseis],']',
            '[',circ[8 + mult_dezeseis], circ[9 + mult_dezeseis],']', 
            '[',circ[10 + mult_dezeseis], circ[11 + mult_dezeseis],']', 
            '[',circ[12 + mult_dezeseis], circ[13 + mult_dezeseis],']', 
            '[',circ[14 + mult_dezeseis], circ[15 + mult_dezeseis],']'
            )
        #print(circ)
        print('------------------------------------')
        print()
    mult_dezeseis = mult_dezeseis + 16

#print(circ)
#print(len(circ)/2)
print(count)

window = pyglet.window.Window()

@window.event
def on_draw():
    global circ
    pyglet.graphics.draw(int(len(circ)/2),pyglet.gl.GL_POINTS,('v2i', circ))


pyglet.app.run()


'''
Os métodos paramétricos e simétricos para a geração de circunferências vão montando a circunf. a partir da
variação angular; o que impacta no raio; já o algoritmo de Bresenhem resolve isso.
'''

'''
-Dúvida: No algoritmo cujo arquivo tem nome "metodo_bresenham_octante" é a junção dos algoritmos de Bresenham p/ circunferência + Método Simétrico de 1 octante, certo?
Por que eles juntaram os dois algoritmos mesmo e qual a vantagem disso?
-Resposta: Sim, bresenhem faz uso da simetria de 1 octante (que é metade de 1 quadrante), ele faz isso pq já existia a técnica de simetria por 1 quadrante, e evoluir para
1 octante. A vantagem é que ao calcular 1 ponto, é possível descobrir mais 7 pontos pela simetria por octante.. Com a simetria de 1 quadrante ao calcular 1 ponto é 
é possível descobrir mais 3 pontos apenas.


-Dúvida: Por acaso o senhor não teria o algoritmo de Bresenham simetria por 1 quadrante em python, né?
-Resposta: Bastaria remover a parte do algoritmo que faz a simetria por octante, ou seja, a que inverte as posição de (x,y), para (y,x). Você notará que o algoritmo
consegue realizar a construção da circunferência mesmo removendo essa parte (ou seja, com simetria de 1 quadrante), isso se dá porque o critério de parada
do algoritmo está enquanto y>=0, ou seja a circunferência inicia com y=raio e vai até y=0, ele calcula 1 quadrante completo da circunferência. Para fazer uso da 
eficácia de 1 octante, o critério de parada teria que ser outro, teria que descobrir inicialmente qual o ponto da circunferência a um ângulo de 45º, e utilizar esse 
ponto para obter o valor do y inicial para o critério de parada do algoritmo. Esse cálculo poderia ser feito através de relações trigonométricas antes de entrar na 
estrutura de repetição.
'''