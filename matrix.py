class Matrix(object):

    lines = 0
    columms = 0
    body = []
    
    def __init__(self, lines, columms):
        self.lines = lines
        self.columms = columms
        self.body = self.gerar(lines, columms)

    def gerar(self, lines, columms):
        gerada = []
        for _ in range(lines):
            gerada.append([" "] * columms)
        return gerada

    def show(self):
        return print(self.body)

    def isSquare(self):
        if (self.lines == self.columms) or (self.columms == self.lines):
            return True
        else:
            return False

    def fill(self):
        for line in range(self.lines):
            for columm in range(self.columms):
                self.element = int(input
                                   (f"Digite um valor na posição [{line}][{columm}]: "
                                    .format([line], [columm])))
                self.body[line][columm] = self.element
        return self.body

    def pDiagonal(self):
        if self.isSquare():
            diagonal_principal = []
            for i in range(len(self.body)):
                diagonal_principal.append(self.body[i][i])
            return diagonal_principal
        else:
            return "matriz não quadradas não possuem diagonal principal"

    def sDiagonal(self):
        if self.isSquare():
            diagonal_secundaria = []
            for i in range(self.lines):
                for j in range(self.columms):
                    if i == self.columms - 1 - j:
                        diagonal_secundaria.append(self.body[i][j])
            return diagonal_secundaria
        else:
            return "matriz não quadradas não possuem diagonal secundária"

    def multDiagonalPrincipal(self):
        produto = 1
        for numero in self.pDiagonal():
            produto *= numero
        return produto

    def xDiagonal(self, mult):
        if self.isSquare():
            mult = [i * mult for i in self.pDiagonal()]
            return mult
        else:
            return "matriz não quadradas não possuem diagonal principal"

    def feature(self):
        if self.isSquare():
            return sum(self.pDiagonal())
        else:
            return "matriz não quadradas não possuem traço"

    def transpoose(self):
        mat_transpoose = list(map(lambda *i: [j for j in i], *self.body))
        self.body = mat_transpoose
        return self.body

    def det(self):
        if self.isSquare():
            if (self.lines == 2) and (self.columms == 2):
                return sum(self.pDiagonal()) - sum(self.sDiagonal())
            else:
                pass

    def sum(self, sumMatrix):
        if (self.lines == sumMatrix.lines) and (self.columms == sumMatrix.columms):
            Soma = Matrix(self.lines, self.columms)
            for i in range(self.lines):
                for j in range(self.columms):
                    Soma.body[i][j] = self.body[i][j] + sumMatrix.body[i][j]
            return Soma.body
        else:
            return "Matrizes de tamanho diferentes não podem ser somadas"

    def mult(self,b_mat):
        c_mat = Matrix (self.lines, b_mat.columms)
        if self.lines == b_mat.columms:
            for lin in range(self.lines):
                for col in range(b_mat.columms):
                    value = 0
                    for i in range(self.columms):
                       value += self.body[lin][i] * b_mat.body[i][col]
                    c_mat.body[lin][col] = value
            return c_mat.body
        else:
            return "Matrizes imcopatíveis para multiplicar"

            
