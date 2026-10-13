
function analisarTurma(notas) {
    if (!Array.isArray(notas) || notas.length === 0) {
        throw new Error("Informe uma lista não vazia.");
    }

    for (const nota of notas) {
        if (typeof nota !== "number" ||
            !Number.isFinite(nota) ||
            nota < 0 || nota > 10) {
            throw new Error("Nota inválida: " + nota);
        }
    }

    const soma = notas.reduce((total, nota) => total + nota, 0);
    const media = soma / notas.length;

    return {
        quantidade: notas.length,
        media,
        maior: Math.max(...notas),
        menor: Math.min(...notas),
        aprovados: notas.filter(nota => nota >= 7).length,
        recuperacao: notas.filter(
            nota => nota >= 5 && nota < 7
        ).length,
        reprovados: notas.filter(nota => nota < 5).length
    };
}

const notas = [8.5, 6.0, 9.0, 4.5, 7.0, 5.5, 3.0];
console.log(analisarTurma(notas));
