class Turma:
    def __init__(self, notas):
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

turma = Turma([8.0, 7.0, 9.0])
print(turma.calcular_media())