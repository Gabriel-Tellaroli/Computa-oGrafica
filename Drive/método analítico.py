import pyglet

window = pyglet.window.Window()
'''
funciona p linhas horizontais, verticais ou inclinidas em 45º, pois não será afetado pela necessidade
de arredondamento a partir da escolha dos pixels a serem usados, evitando o aliasing ou o "Pulo" de alguns pixels
Custo de processamento considerável devido às operações de divisão e arredondamento a cada ponto.

    - Pontilhamento: muito espaçamento entre um ponto e outro
    - Aliasing: "escadinha" na reta

Usa das seguintes equações:
 - Equação reduzida da reta
        y = m * x + b

 - Coeficiente angular
        m = (y2 - y1) / (x2 - x1)
            Obs.: caso a reta esteja na VERTICAL, o coef.
                    angular não existe

 - Deslocamento
        b = y2 - m * x2
'''

'''
Exemplo encontrando os pontos
p1 = [10, 10]
p2 = [13, 12]

m = (12-10)/(13-10) = 2/3 = 0,667
b = 12 - 0,667*13 = 3,33

X = 10:		Y = 0,667*10 + 3,33	= 10		[10, 10]
X = 11:		Y = 0,667*11 + 3,33 = 11		[11, 11]
X = 12:		Y = 0,667*12 + 3,33 = 11		[12, 11]
X = 13:		Y = 0,667*13 + 3,33 = 12		[13, 12]
'''

'''
ALG:
% reta vertical
x1 = x2

se sim:                   Ou seja, a reta está na vertical
    para Y de Y1 até Y2
        liga_pixel(X1, Y, Cor)
    
senão:
    m = (Y2 - Y1)/(X2-X1)
    b = Y2 - m * X2
    para X de X1 até X2
        Y = m * X + b
        liga_pixel(X, Y, Cor)

'''

#coordenadas iniciais da reta
p1 = [10, 10]
p2 = [13, 12]

#Validação para casos onde a reta é desenhada pelo usuário da direita
#para a esquerda, inverte-se o valor de P2 e P1
if p1[0]>p2[0]:
    x = p2[0]
    y = p2[1]
    p2[0] = p1[0]
    p2[1] = p1[1]
    p1[0] = x
    p1[1] = y

x = p1[0]
y = p1[1]

#m = coeficiente angular
if p1[0] != p2[0]:
    m = (p2[1]-p1[1]) / (p2[0]-p1[0]) #(Y2 - Y1)/(X2 - X1)
else:
    m = 0   #caso seja igual, apenas atribuindo zero para não dar erro na interpretação do prog

b = p2[1] - m * p2[0]                 #Y2 - m * X2, b = deslocamento

def update(dt):
    global x,y,p1,p2
    if p1[0] == p2[0] and y <= p2[1]:   #para Y de Y1 até Y2
        print(x, y)
        y += 1                  #incrementa y para executar como se fosse um loop, pelas chamadas de update
    elif x <= p2[0]:            #para X de X1 até X2
        print(x, y)
        x += 1                  #incrementa x para executar como se fosse um loop, pelas chamadas de update
        y = round(m * x + b)    # Y = m * X + b, tal que X = valor do X atual//isto é, eq reduzida da reta



pyglet.clock.schedule_interval(update,1/90) #chama update a cada 90 vezes por segundo

@window.event
def on_draw():
    pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,('v2i',(x,y)))

pyglet.app.run()
