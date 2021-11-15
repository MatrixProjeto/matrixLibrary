class Matrix(object):

    def __init__(self, lines, columms):
        self.lines = lines
        self.columms = columms
        self.body = self.gerar(lines, columms)

    def gerar(self,lines, columms):
        gerada = []
        for _ in range(lines):
            gerada.append([" "] * columms)
        return gerada

    def show(self):
        print(self.body)

    def isSquare(self):
        if (self.lines == self.columms) or (self.columms == self.lines):
            return True
        else:
            return False

    def fill(self):
        for line in range(self.lines):
            for columm in range(self.columms):
                self.element = int(input(f"Digite um valor na posição [{line}][{columm}]: ".format([line], [columm])))
                self.body[line][columm] = self.element

    def pDiagonal(self):
        if self.isSquare():
            diagonal_principal = []
            for i in range(len(self.body)):
                diagonal_principal.append(self.body[i][i])
            return diagonal_principal
        else:
            return "matriz não quadradas não possuem diagonal principal"

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

    def sum(self, sumMatrix):
        pass

    def mult(self, multMatrix):
        pass