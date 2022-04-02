'''
Características do Método Analítico
– Funciona bem para linhas horizontais,
verticais ou inclinadas 45º;
– Para outras linhas é necessário decidir o
melhor pixel a ser usado;
– Aparência de serrilhado (aliasing);
– Requer considerável custo de processamento.
'''

import pyglet

window = pyglet.window.Window()


#coordenadas iniciais da reta
p1 = [10, 10]
p2 = [13, 12]

if p1[0]>p2[0]:
    x = p2[0]
    y = p2[1]
    p2[0] = p1[0]
    p2[1] = p1[1]
    p1[0] = x
    p1[1] = y

x = p1[0]
y = p1[1]

m = (p2[1]-p1[1]) / (p2[0]-p1[0])
b = p2[1] - m * p2[0]

def update(dt):
    global x,y,p1,p2
    if p1[0] == p2[0] and y <= p2[1]:
        y += 1
    elif x <= p2[0]:
        x += 1
        y = round(m * x + b)
    print(x,y)


pyglet.clock.schedule_interval(update,1/90) #chama update a cada 90 vezes por segundo

@window.event
def on_draw():
    pyglet.graphics.draw(1,pyglet.gl.GL_POINTS,('v2i',(x,y)))

pyglet.app.run()