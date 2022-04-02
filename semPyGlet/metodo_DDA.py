import pyglet

#coordenadas iniciais da reta
#      x  y
p1 = [10,10]
p2 = [13,12]

dx = abs(p2[0] - p1[0])
dy = abs(p2[1] - p1[1])

reta = []

if dx == 0:
    for y in range(p1[1], p2[1]):
        reta.append(p1[0])
        reta.append(y)
elif dy == 0:
    for x in range(p1[0], p2[0]):
        reta.append(x)
        reta.append(p1[1])
elif dx > dy:
    inc = dy / dx
    ini = p1[0]
    fim = p2[0]
    y = p1[1]
    if p1[0] > p2[0]:
        y = p2[1]
        ini = p2[0]
        fim = p1[0]
    for x in range(ini, fim):
        reta.append(x)
        reta.append(round(y))
        y = y+inc
else:
    inc = dx / dy
    x = p1[0]
    ini = p1[1]
    fim = p2[1]
    if p1[1] > p2[1]:
        x = p2[0]
        ini = p2[1]
        fim = p1[1]
    for y in range(ini, fim):
        reta.append(round(x))
        reta.append(y)
        x = x+inc

# Adicionando o P2 ou ultimo ponto
reta.append(p2)

print(reta)