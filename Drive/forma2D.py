import pyglet
import math

# vertices da forma
forma = [(200, 200), (300, 100), (400, 200)]
batch = pyglet.graphics.Batch()
vertices = [] #armazena o vertex_list

# desenha o poligono desenhando as retas
def draw_poligon(forma2D):
    #apaga a lista de vertices da forma desenhada
    if len(vertices) != 0:
        for vertex_list in vertices:
            vertex_list.delete()
        vertices.clear()

    #indica os vertices das retas que formam o poligono
    for i in range(0, len(forma2D)-1):
        p1 = forma2D[i]
        p2 = forma2D[i+1]
        #para fazer uma linha
        vertices.append(batch.add(2, pyglet.gl.GL_LINES, None, ('v2i', (p1[0], p1[1], p2[0], p2[1]))))

    #para conectar a ultima reta
    p1 = forma2D[len(forma2D)-1]
    p2 = forma2D[0]
    vertices.append(batch.add(2, pyglet.gl.GL_LINES, None, ('v2i', (p1[0], p1[1], p2[0], p2[1]))))

#desenha o poligono inicial
draw_poligon(forma)

#cria a janela do pyglet
window = pyglet.window.Window()

#trata os eventos de pressionamento das teclas
@window.event
def on_key_press(symbol, modifiers):
    global forma
    if symbol == pyglet.window.key.RIGHT:
        print("->")
        forma_t = []
        for p in forma:
            forma_t.append((p[0]+10,p[1]))
        forma = forma_t
    elif symbol == pyglet.window.key.LEFT:
        print("<-")
        forma_t = []
        for p in forma:
            forma_t.append((p[0]-10, p[1]))
        forma = forma_t
    elif symbol == pyglet.window.key.UP:
        print("^")
        forma_t = []
        for p in forma:
            forma_t.append((p[0], p[1]+10))
        forma = forma_t
    elif symbol == pyglet.window.key.DOWN:
        print("v")
        forma_t = []
        for p in forma:
            forma_t.append((p[0], p[1]-10))
        forma = forma_t
    elif symbol == pyglet.window.key.Y: #escalar
        print("Y")
        x=0
        y=0
        for p in forma:
            x += p[0]
            y += p[1]
        xref = x / len(forma) #x pm
        yref = y / len(forma) #y pm

        forma_t = []
        for p in forma:
            #passo 1
            x = p[0] - xref
            y = p[1] - yref

            #passo 2
            x *= 0.5    #escala x
            y *= 0.5    #escala y

            #passo 3
            x += xref
            y += yref

            forma_t.append((int(x), int(y)))
        forma = forma_t
    elif symbol == pyglet.window.key.R: #rotacionar
        print("R")
        x=0
        y=0
        for p in forma:
            x += p[0]
            y += p[1]
        xref = x / len(forma)
        yref = y / len(forma)

        forma_t = []
        rad = 90 * math.pi/180  #para alterar o grau mude o "90"

        for p in forma:
            x = p[0] - xref
            y = p[1] - yref

            xr = x * math.cos(rad) - y * math.sin(rad)
            yr = x * math.sin(rad) + y * math.cos(rad)

            xr += xref
            yr += yref

            forma_t.append((int(xr), int(yr)))

        forma = forma_t
    elif symbol == pyglet.window.key.E: #espelhar
        print("E")
        x = 0
        y = 0
        for p in forma:
            x += p[0]
            y += p[1]
        xref = x / len(forma)
        yref = y / len(forma)

        forma_t = []

        for p in forma:
            x = p[0] - xref
            y = p[1] - yref

            x *= -1
            y *= 1

            x += xref
            y += yref

            forma_t.append((int(x), int(y)))
        forma = forma_t

    draw_poligon(forma)

#Desenha a tela
@window.event
def on_draw():
    window.clear()
    pyglet.gl.glClear(pyglet.gl.GL_COLOR_BUFFER_BIT)
    batch.draw()
    print(forma)

pyglet.app.run()


'''
TRANSLADAR: “movimentar o objeto”

somar a matriz com os vértices e a matriz do translado

Ex.: transladar uma reta P1(10,10) e P2(10,100) em 100 pontos
no eixo x, e 50 pontos no eixo y:

reta = 10   10
       10   100

trans = 100 50
        100 50

retaT = reta + trans

retaFinal = 110 60
            110 150
Ou seja, basta realizar a soma vetorial dos pontos


No Translado, se a gente soma em x estamos transladando para a direita; se a gente soma em y, estamos transladando para cima; e vice-versa (referente à esquerda)
'''

'''
ESCALONAR: “mudar as dimensões de escala”

multiplicar a matriz com os vértices pela matriz matriz de fatores de escala Sx e Sy, mas assim ocorrerá
um translado indesejado

Representação matricial:
[x y] *| Sx  0 |
       | 0   Sy|

O escalonamento do objeto acaba gerando uma translação

Ex.: escalonar uma reta P1(10,10) e P2(10,100) em 2 pontos no
eixo x, e 2 pontos no eixo y

reta = 10   10
       10   100

trans = 2 0
        0 2

retaT = reta * trans

retaFinal = 20 20
            20 200

para evitar o translado indesejado basta:
1 transladar para o ponto médio (isso é, matriz dos vértices - ponto médio) onde ponto médio = soma dos
pontos[x, y]/núm de vértices
2 realizar a escala (multiplicação do resultado do passo 1 pelos fatores de escala)
3 Transladar novamente para o ponto médio, isto é, somar o resultado do passo 2 pela matriz com o ponto médio

'''

''' 
ROTAÇÃO:

para evitar a translação do objeto rotacionado, basta movê-lo para a origem, rotacioná-lo e depois transladá-lo novamente para a posição inicial

[x' y']= [x y] * cos(angulo)    sen(angulo)
                 -sen(angulo)   cos(angulo)

x' = x cos(angulo) - y sen(angulo)
y' = y cos(angulo) + x sen(angulo)
'''

'''
ESPELHAR: "Mover o objeto de maneira que o mesmo reflita a sua imagem no eixo x, y ou xy"

Sem transladar, é só alterar o sinal do que vc quer mexer. Por ex.: quero espelhar em X, então vou mudar os sinais do Y
pq quem é alterado é o Y. o X permanece.

Basta multiplicar os pontos pela matriz abaixo, deixando negativos as linhas e colunas em que se deixar realizar o espelhamento

[x' y']= [x y] * 1    0
                 0   -1

Matriz de espelhamento (x y):
        -1 0
         0 -1
Matriz de espelhamento em y:
        -1 0
         0 1

Na Matriz de Espelhamento:
    Se quiser **manter** a coordenada X OU Y: coloca 1
    Se quiser **espelhar** a coordenada X OU Y: coloca -1

Quando:
    Espelho em X: estou mantendo o X, mudando o Y (forma muda na vertical)
    Espelho em Y: estou mantendo o Y, mudando o X (forma muda na horizontal)
'''

'''
Com translado indesejado:
100 100	*	0,5 0		=	50 50
100 200	*	0 0,5		=	50 100
200 100	*			=	100 50

Sem translado indesejado:

ponto médio (pm) = (133,33, 133,33) (soma dos pontos[x, y]/núm de vértices)

A gente translada para o ponto médio:
(pontos
antigos)
100 100	 	133,33 133,33	  	-33,33 -33,33
100 200	-	133,33 133,33	=	-33,33 66,67
200 100	 	133,33 133,33	 	66,67 -33,33

Realiza a escala
-33,33 -33,33	*	0,5 0		=	-16,665 -16,665
-33,33 66,67	*	0 0,5		=	-16,665 33,335
66,67 -33,33	*			=	33,335 -16,665

Translada novamente para o ponto médio:
-16,665 -16,665	+	133,33 133,33	=	117 117
-16,665 33,335	+	133,33 133,33	=	117 167
33,335 -16,665	+	133,33 133,33	=	167 117

'''