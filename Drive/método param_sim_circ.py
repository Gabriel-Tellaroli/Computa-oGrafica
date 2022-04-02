'''
Através de dois pontos: P1 - ponto central da circ; P2 - ponto pertencente a circ.

Baseia-se na propriedade de simetria da circ, calculando apenas os pontos de 1 quadrante; onde os demais são calculados
através de simetria.
'''

'''
Diminui a quantidade de cálculos trigonométricos, comparados ao paramétrico; mas ainda utiliza um pouco e a densidade
dos pontos tb varia com o raio.

Conclusão: quanto maior o ângulo, a depender do raio gerado pela circunferência cujos pontos foram dados, podemos nos deparar com os problemas do efeito pontilhado. Relacionando-se com o “encontro” dos pixels no ponto central.
'''

'''
DISPOSIÇÃO DOS QUADRANTES:

        QII  (-x , y)        |       QI  (x , y)
    _________________________|_________________________
                             |
        QIII (-x , -y)       |       QIV (x , -y)

'''

'''
ALG:

raio = √(x1−x2)²+(y1−y2)²
delta_t = pi / 180
para t = 0 até pi / 2 com passo delta_t  ** O "pi/2" é pelo fato de só calcularmos 1 quadrante
    x = arredonda(raio · cos(t))
    y = arredonda(raio · sen(t))
    ligue(x+x1, y+y1)
    ligue(-x+x1, y+y1)
    ligue(-x+x1, -y+y1)
    ligue(x+x1, -y+y1)
próximo t
'''

'''
EXEMPLO
P1(50, 50)
P2(55, 50)

raio: 5
delta_pi: 0,008726

while (t <= 2pi):
	x = round(raio*cos(t)) = (5*1) = 5
	y = round(raio*sin(t)) = (5*0) = 0

	primeiro quadrante: (50, 50) + (5, 0) = (55, 50)
	quarto quadrante: (50, 50) + (5, -0) = (55, 50)
	segundo quadrante: (50, 50) + (-5, 0) = (45, 50)
	terceiro quadrante: (50, 50) + (-5, -0) = (45, 50)

	t += delta_pi = 0,008726
------------------
	x = round(raio*cos(t)) = (5*0,999999) = 5
	y = round(raio*sin(t)) = (5*0,008726) = 0,04363 = 0

	primeiro quadrante: (50, 50) + (5, 0) = (55, 50)
	quarto quadrante: (50, 50) + (5, -0) = (55, 50)
	segundo quadrante: (50, 50) + (-5, 0) = (45, 50)
	terceiro quadrante: (50, 50) + (-5, -0) = (45, 50)

	t += delta_pi = 0,017452
------------------
	x = round(raio*cos(t)) = (5*0,999999) = 5
	y = round(raio*sin(t)) = (5*0,017452) = 0,0872 = 0

	primeiro quadrante: (50, 50) + (5, 0) = (55, 50)
	quarto quadrante: (50, 50) + (5, -0) = (55, 50)
	segundo quadrante: (50, 50) + (-5, 0) = (45, 50)
	terceiro quadrante: (50, 50) + (-5, -0) = (45, 50)

	t += delta_pi = 0,026178

parando aqui pq estava querendo somente as 3 primeiras iterações
'''

import pyglet
import math

#coordenadas iniciais da reta
p1 = [int(i) for i in input("Entre com as coordenadas do centro da circunferencia: ").split()]
p2 = [int(i) for i in input("Entre com as coordenadas de um ponto da circunferência: ").split()]

raio = math.sqrt(((p1[0]-p2[0])**2) + ((p1[1]-p2[1])**2)) #√(x1−x2)²+(y1−y2)²

delta_pi = math.pi / 360

circ = []
t = 0
count = 0

# Auxiliares de resultado ( Tella )
n_interacoes = 3
mult_oito = 0

while (t <= (math.pi/2) ):
    x = round(raio*math.cos(t))
    y = round(raio*math.sin(t))
    #primeiro quadrante
    circ.append(p1[0] + x)
    circ.append(p1[1] + y)
    #quarto quadrante
    circ.append(p1[0] + x)
    circ.append(p1[1] - y)
    #segundo quadrante
    circ.append(p1[0] - x)
    circ.append(p1[1] + y)
    #terceiro quadrante
    circ.append(p1[0] - x)
    circ.append(p1[1] - y)


    t += delta_pi
    count += 1  #nº de iterações
    # Edição para visualizar os pontos das *n_interacoes*
    if count <= n_interacoes:
        print('------------------------------------')
        print('Iteracao:',count)
        print(
            '[',circ[0 + mult_oito], circ[1 + mult_oito],']', 
            '[',circ[2 + mult_oito], circ[3 + mult_oito],']', 
            '[',circ[4 + mult_oito], circ[5 + mult_oito],']', 
            '[',circ[6 + mult_oito], circ[7 + mult_oito],']'
            )
        #print(circ)
        print('------------------------------------')
        print()
    mult_oito = mult_oito + 8

#print()
#print(circ)
#print(len(circ)/2)
print(count)

window = pyglet.window.Window()

@window.event
def on_draw():
    global circ
    pyglet.graphics.draw(int(len(circ)/2),pyglet.gl.GL_POINTS,('v2i', circ))


pyglet.app.run()