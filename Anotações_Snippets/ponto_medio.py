import math
 
# função que permite calcular a distância
# entre dois pontos no plano (R2)
def distancia2d(x1, y1, x2, y2, x3, y3):
  a = x3 - x2 - x1
  b = y3 - y2 - y1
  c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
  return c
 
# função principal do programa
def main():
  # vamos ler os dados do primeiro ponto
  x1 = float(input("Informe o x do primeiro ponto: "))
  y1 = float(input("Informe o y do primeiro ponto: "))
     
  # vamos ler os dados do segundo ponto
  x2 = float(input("Informe o x do segundo ponto: "))
  y2 = float(input("Informe o y do segundo ponto: "))

   # vamos ler os dados do terceiro ponto
  x3 = float(input("Informe o x do segundo ponto: "))
  y3 = float(input("Informe o y do segundo ponto: "))
     
  # vamos calcular as coordenadas x e y do ponto médio    
  x = (x1 + x2 + x3) / 3
  y = (y1 + y2 + y3) / 3
 
  # vamos mostrar o resultado
  print("As coordenadas do ponto médio são: (x = %0.1f, y = %0.1f)"
    % (x, y))
   
if __name__== "__main__":
  main()