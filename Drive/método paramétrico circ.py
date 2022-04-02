'''
random info:
SRU (Sistema de Referência do Universo): usa de alguma das coordenadas existentes (Coordenadas Esféricas, Polares, Cilíndricas); são os sistemas que são utilizados pela humanidade;
    Exemplo: sistema de coordenadas do plano cartesiano matemático


SRO (Sistema de Referência do Objeto): utilizado pelo sistema (software).
    Exemplo 1: as coordenadas da margem de um documento Word
    Exemplo 2: as coordenadas do sistema cartesiano do computador (notar que o eixo Y é “invertido” se comparado ao sistema cartesiano matemático)


SRN (Sistema de Referência Normatizado): sistema normatizado com valores entre 0 e 1, independente do dispositivo;

SRD (Sistema de Referência do Dispositivo): utilizado como mecanismo de saída, ex.: impressora, monitor etc.
    Exemplo: o driver de uma impressora realiza a “conversão” da coordenada do pixel X (que estava no SRO) para a coordenada que deve ficar no papel (SRD)

SCU -> Sistemas de Coordenadas do Universo
SCO -> Sistemas de Coordenadas do Objeto
SCD -> Sistemas de Coordenadas do Dispositivo

----------------------
-IMPORTANTE: o centro da circunf NÃO é a origem doo gráfico.
Caso coloque o “centro da circunferência” como sendo a origem do gráfico, ou seja, as coordenadas (0, 0),
ele desenharia apenas uma parte da circunferência

Possuem problemas similares com os das retas, só que aqui há + a complex. dos cálculos das func. trigonométricas
O Algoritmo paramétrico são necessários 2 pontos, o ponto central, e um ponto presente na circunferência.

OBS.:
*Um dos problemas desse ALG é que ele usa as func trigonométricas e a densidade dos pontos varia com o raio:
O Delta_PI impacta diretamente na localização dos pontos da circunferência. Para circunferências maiores,
quanto maior o Delta_PI, melhor, pois evita o efeito de pontilhamento

*Como vão ter mais pontos, a distância entre entre eles nas bordas da circunferência serão menores, e consequentemente,
o efeito de pontilhamento desaparece
    - Pontilhamento: muito espaçamento entre um ponto e outro
    - Aliasing: "escadinha" na reta

*Para “aumentar” ou “diminuir” o Delta_PI, basta alterar o valor do divisor

*Quanto maior o Delta_PI, isto é, menor o divisor, obtemos menos pontos, porém, dependendo do tamanho da circunf:
quanto maior a circunf e menor o Delta_PI, maiores as chances de nos depararmos com efeito de pontilhamento

Conclusão: quanto maior o ângulo, a depender do raio gerado pela circunferência cujos pontos foram dados, podemos nos deparar com os problemas do efeito pontilhado. Relacionando-se com o “encontro” dos pixels no ponto central.
'''

'''
Conversão de graus em radianos e vice versa: pí rad = 180º. Aplicar regra de 3
ou de rad para graus (macete ex: 2/3 pi rad para graus):
2/3 pi rad = 2/3 * 180
2/3 * 180 = 360/3 = 120.
'''

'''
ALG:
x1, y1 deve ser o centro da circunf.
x2, y2 deve ser um ponto da circunf.

Deverá ser calculado o raio da circunferência;
E gerar pontos (x, y) onde o ângulo t deve variar de 0 a 2pi
---
x <= raio
y = 0

para t de 1 até 360:
    pixel(x, y, cor)
    x = r * cos((pi*t)/180)
    y = r * sen((pi*t)/180)
'''


'''
EXEMPLO
P1(50, 50)
P2(55, 50)

raio = 5
delta_pi = 0,008726

while(t <= (2*pi))
	x = x + round(raio*cos(t)) = 50 + round(5*cos(0)) = 55
	y = y + round(raio*sin(t)) = 50 + round(5*sin(0)) = 50

	(55, 50)

	t += 0,008726
	--------------------
	x = x + round(raio*cos(t)) = 50 + round(5*cos(0,008726)) = 55
	y = y + round(raio*sin(t)) = 50 + round(5*sin(0,008726)) = 50

	(55, 50)

	t += 0,017452
	-------------------
	x = x + round(raio*cos(t)) = 50 + round(5*cos(0,017452)) = 55
	y = y + round(raio*sin(t)) = 50 + round(5*sin(0,017452)) = 50

	(55, 50)

	t += 0,026178

	parando aq pois pediu os 3 primeiros pontos
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

# Auxiliares de resultado ( Tella )
n_interacoes = 3
count = 0
mult_dois = 0

while (t <= (2*math.pi) ):
    x = p1[0]+round(raio*math.cos(t))
    y = p1[1]+round(raio*math.sin(t))
    circ.append(x)
    circ.append(y)
    t += delta_pi
    
    # Edição para visualizar os pontos das *n_interacoes*
    count += 1
    if count <= n_interacoes:
        print('------------------------------------')
        print('Iteracao:',count)
        print('[',circ[0 + mult_dois], circ[1 + mult_dois],']')
        #print(circ)
        print('------------------------------------')
        print()
    mult_dois = mult_dois + 2
print(circ)
print(len(circ)/2)
window = pyglet.window.Window()

@window.event
def on_draw():
    global circ
    pyglet.graphics.draw(int(len(circ)/2),pyglet.gl.GL_POINTS,('v2i', circ))


pyglet.app.run()