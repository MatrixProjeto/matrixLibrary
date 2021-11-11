class Matrix ():
    body = []

    def __init__(self, lines, columms):
        self.lines = lines
        self.columms = columms
        self.__gerar()

    def __gerar(self):
        for _ in range(self.lines):
            self.body.append([" "] * self.columms)

    def show (self):
        for j in self.body:
            return j

    def fill (self):
        for line in range(self.lines):
            for columm in range(self.columms):
                self.element = int(input("Digite um valor: "))
                self.body[line][columm] = self.element
    
    def pDiagonal (self):
        diagonal_principal = []
        for i in range(len(self.body)):
            diagonal_principal.append(self.body[i][i])
        return diagonal_principal
            
    def xDiagonal (self, mult):
        for i in range(len(self.body)):
            self.body[i][i] *= mult

    def transpoose (self):
        mat_transpoose = list(map(lambda *i: [j for j in i], *self.body))
        return mat_transpoose