class Matriz:
    def __init__(self, mat):
        self.mat = mat
        self.lin = len(mat)
        self.col = len(mat[0])

    def getLinha(self, n):
        return [i for i in self.mat[n]]

    def getColuna(self, n):
        return [i[n] for i in self.mat]

    # opcional: dar overload no operador de multiplicação
    def __mul__(self, mat2):
        matRes = []

        for i in range(self.lin):           
            matRes.append([])

            for j in range(mat2.col):
                listMult = [x*y for x, y in zip(self.getLinha(i), mat2.getColuna(j))]
                matRes[i].append(sum(listMult))

        return matRes

mat1 = Matriz([[200,200],[300,100],[400,200]])
mat2 = Matriz([[0.5,0], [0,0.5]])
print(mat1*mat2)