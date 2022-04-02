import pyglet

'''
Dynamic Dcay Adjustment
equação diferencial da reta.
Processamento: um pouco melhor que o Analítico, mas ainda possui baixa performance pois há divisões,
que é uma operação custosa; e ainda há aliasing: pq possui problemas de truncamento e arredondamento.

O DDA é muito semelhante ao Analítico, diferenciando em
termos de implementação e performance
'''

'''
Exemplo encontrando os pontos
p1 = [10, 10]
p2 = [13, 12]

(x2 - x1) > (y2 - y1)?
(13 - 10) > (12 - 10) = 3 > 2 = SIM
então:
Incr = (12 - 10)/(13 - 10) = 0,667
Y = 10

X = 10:		[10, 10]
			Y = Y + Incr = Y = 10 + 0,667 = 10,667
			Arredonda Y = 10,667 para montar a próx coordenada = 11
X = 11:		[11, 11]
			Y = Y + Incr = Y = 10,667 + 0,667 = 11,334
			Arredonda Y = 11,334 para montar a próx coordenada = 11
X = 12:		[12, 11]
			Y = Y + Incr = Y = 11,334 + 0,667 = 12,001
			Arredonda Y = 12,001 para montar a próx coordenada = 12
X = 13:		[13, 12]
			Y = Y + Incr = Y = 12,001 + 0,667 = 12,668 = 13

OBS.: o cálculo deve considerar o arredondamento somente para formar a coord, o valor do y para o próx incremento NÃO será arredondado.
'''

'''
ALG:
(X2 - X1) > (Y2 - Y1) ?
Se sim:
    Incr <- (Y2 - Y1)/(X2-X1)
    Y <- YI
    
    para X de X1 até X2
        liga_pixel(X, Y, Cor) #aqui é necessário arredondar o Y para montar as próxs coord
        Y <- Y + Incr         #aqui é o valor sem arredondamento, do Y msm
        
Senão:
    Incr <- (X2 - X1)/(Y2 - Y1)
    X <- X1
    
    para Y de Y1 até Y2
        liga_pixel(X, Y, Cor) #aqui é necessário arredondar o X para montar as próxs coord
        X <- X + Incr         #aqui é o valor sem arredondamento, do X msm
'''

#coordenadas iniciais da reta
p1 = [int(i) for i in input("Entre com as coordenadas de P1 x y: ").split()]
p2 = [int(i) for i in input("Entre com as coordenadas de P2 x y: ").split()]

dx = abs(p2[0] - p1[0])
dy = abs(p2[1] - p1[1])

reta = []

if dx == 0: #reta posição vertical
    for y in range(p1[1], p2[1]):
        reta.append(p1[0])
        reta.append(y)
elif dy == 0: #reta posição horizontal
    for x in range(p1[0], p2[0]):
        reta.append(x)
        reta.append(p1[1])
elif dx > dy:
    inc = dy / dx
    ini = p1[0]
    fim = p2[0]
    y = p1[1]
    if p1[0] > p2[0]:   #se for (50, 50) e (30,40) por exemplo, entrará aqui, para que comecemos do ponto + a esq
        y = p2[1]
        ini = p2[0]
        fim = p1[0]
    for x in range(ini, fim+1):
        reta.append(x)
        reta.append(round(y))   #arredonda apenas para montar o ponto da coord
        y = y+inc
else:
    inc = dx / dy
    x = p1[0]
    ini = p1[1]
    fim = p2[1]
    if p1[1] > p2[1]:   #se for (50, 50) e (30,40) por exemplo, entrará aqui, para que comecemos do ponto + a esq
        x = p2[0]
        ini = p2[1]
        fim = p1[1]
    for y in range(ini, fim+1):
        reta.append(round(x))   #arredonda apenas para montar o ponto da coord
        reta.append(y)
        x = x+inc

print(reta)
window = pyglet.window.Window()

@window.event
def on_draw():
    global reta
    pyglet.graphics.draw(int(len(reta)/2),pyglet.gl.GL_POINTS,('v2i', reta))


pyglet.app.run()