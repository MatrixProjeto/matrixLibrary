
from matrix import Matrix

Teste = Matrix(2,2)

Teste.fill()
print(Teste.show())
print(Teste.transpoose())
print(Teste.pDiagonal())
Teste.xDiagonal(3)
print(Teste.show())