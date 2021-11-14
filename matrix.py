class Matrix(object):

    def __init__(self, lines, columms):
        self.lines = lines
        self.columms = columms
        self.body = self.gerar(lines, columms)

    def gerar(self,lines, columms):
        m = []
        for _ in range(lines):
            m.append([" "] * columms)
        return m

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
                self.element = int(input("Digite um valor: "))
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
            for i in range(len(self.body)):
                self.body[i][i] *= mult
        else:
            return "matriz não quadradas não possuem diagonal principal"

    def transpoose(self):
        mat_transpoose = list(map(lambda *i: [j for j in i], *self.body))
        self.body = mat_transpoose
        return self.body

    def sum(self, sumMatrix):
        pass

    def mult(self, multMatrix):
        pass