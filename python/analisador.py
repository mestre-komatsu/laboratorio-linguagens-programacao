
def validar_notas(notas):
    if not notas:
        raise ValueError("A lista de notas não pode estar vazia.")

    for nota in notas:
        if not isinstance(nota, (int, float)):
            raise TypeError("Todas as notas devem ser numéricas.")
        if not 0 <= nota <= 10:
            raise ValueError("As notas devem estar entre 0 e 10.")

def analisar_turma(notas):
    validar_notas(notas)

    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)

    aprovados = sum(nota >= 7 for nota in notas)
    recuperacao = sum(5 <= nota < 7 for nota in notas)
    reprovados = sum(nota < 5 for nota in notas)

    return {
        "quantidade": len(notas),
        "media": media,
        "maior": maior,
        "menor": menor,
        "aprovados": aprovados,
        "recuperacao": recuperacao,
        "reprovados": reprovados,
    }

notas = [8.5, 6.0, 9.0, 4.5, 7.0, 5.5, 3.0]

resultado = analisar_turma(notas)

for indicador, valor in resultado.items():
    if isinstance(valor, float):
        print(f"{indicador}: {valor:.2f}")
    else:
        print(f"{indicador}: {valor}")
