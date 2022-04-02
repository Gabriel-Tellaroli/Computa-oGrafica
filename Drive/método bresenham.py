import pyglet
'''
Clássico da CG. É um AG Incremental que usa somente soma e subtração de inteiros.
Se baseia na decisão de se o próximo pixel terá coord (x+1, y) ou (x+1, y+1).
A decisão será feita através da avaliação se a linha passa acima ou abaixo do PM (x+1, y+1/2)

É mais performático que os anteriores (menor custo operacional)
Mesmo que utilize de multiplicação, só está usando multiplicação por 2 (que, em suma, é apenas uma soma de X + X, que não gera grande custo)

'''

'''
Exemplo encontrando os pontos
p1 = [10, 10]
p2 = [13, 12]

x = x0 = 10
y = y0 = 10

dy = y1 - y0 = 12 - 10 = 2
dx = x1 - x0 = 13 - 10 = 3

d = 2 * dy - dx = 2 * 2 - 3 = 1

LOOP (para i = 0 até dx, pois dx > dy):
i = 0:
	[10, 10]
	d > 0 ? SIM
		y = y + 1 = 10 + 1 = 11
		d = d + 2(dy - dx) = 1 + 2(2 - 3) = 1 - 2 = -1

	x = x + 1 = 10 + 1 = 11

i = 1:
	[11, 11]
	d > 0 ? NÃO
		d = d + 2dy = -1 + 2*2 = -1 + 4 = 3
	x = x + 1 = 11 + 1 = 12

i = 2:
	[12, 11]
	d > 0 ? SIM
		y = y + 1 = 11 + 1 = 12
		d = d + 2(dy - dx) = 3 + 2(2 - 3) = 1
	x = x + 1 = 12 + 1 = 13

i = 3:
	[13, 12]
	d > 0 ? SIM
		y = y + 1 = 12 + 1 = 13
		d = d + 2(dy - dx) = 1 + 2(2 - 3) = 1 - 2 = -1
para o algoritmo pq i = dx (3)

'''

'''
ALG:
x = x0
y = y0

dy = y1-y0
dx = x1-x0

d = 2 * dy - dx

Para i = 0 até dx (ou dy, dependerá de quem for maior)
    ligarPixel(x, y)
    Se d > 0
        y = y + 1
        d = d + 2(dy - dx)
    Senão:
        d = d + 2dy
    x = x + 1
'''

#coordenadas iniciais da reta
p1 = [50,50]
p2 = [55,50]

#     X2      X1
dx = p2[0] - p1[0]
#    Y2       Y1
dy = p2[1] - p1[1]

#(x,y)
x = p1[0]
y = p1[1]

#Lista que conterá as coordenadas (X,Y) de cada ponto da reta
reta = []

if dx == 0: #reta vertical
    for y in range(p1[1], p2[1]): #nesse caso, o x permanece o mesmo e o y será acrescentado conforme iterado
        reta.append(p1[0])
        reta.append(y)
elif dy == 0: #reta horizontal
    for x in range(p1[0], p2[0]): #nesse caso, o y permanece o mesmo e o x será acrescentado conforme iterado
        reta.append(x)
        reta.append(p1[1])
elif dx > dy:
    d = 2 * dy - dx
    for i in range(0, dx+1):
        reta.append(x)
        reta.append(y)
        if d >= 0:
            d = d + 2 * (dy - dx)
            y += 1
        else:
            d += 2 * dy
        x += 1
else:
    d = 2 * dx - dy
    for i in range(0, dy+1):
        reta.append(x)
        reta.append(y)
        if d >= 0:
            d = d + 2 * (dx - dy)
            x += 1
        else:
            d += 2 * dx
        y += 1

print(reta)
window = pyglet.window.Window()

@window.event
def on_draw():
    global reta
    pyglet.graphics.draw(int(len(reta)/2),pyglet.gl.GL_POINTS,('v2i', reta))


pyglet.app.run()

'''
De acordo com o ex de revisão para os pontos (10, 10) e (13, 12):
-Dúvida: Entendo que o Analítico e o DDA sejam semelhantes, mas é normal para os mesmos pontos (P1 e P2) os TRÊS
resultarem na mesma sequência de pontos para formar a reta? Por quê?
-Resp: Para o ângulo de inclinação da reta formada por esses pontos isso é normal, se fosse uma reta maior (com
mais pontos) e uma angulação mais acentuada aí notaríamos maior diferença entre os pontos, principalmente
entre Bresenhem e os demais.
'''

'''
Analítico (performance: 3)
DDA (performance: 2) - resolve o pontilhamento, mas há aliasing
Bresenham (performance: 1), resolve o aliasing
'''