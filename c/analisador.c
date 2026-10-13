
#include <stdio.h>

int main(void) {
    float notas[] = {8.5, 6.0, 9.0, 4.5, 7.0, 5.5, 3.0};
    int quantidade = sizeof(notas) / sizeof(notas[0]);

    float soma = 0.0f;
    float maior = notas[0];
    float menor = notas[0];

    int aprovados = 0;
    int recuperacao = 0;
    int reprovados = 0;

    for (int i = 0; i < quantidade; i++) {
        if (notas[i] < 0 || notas[i] > 10) {
            printf("Nota invalida: %.2f\n", notas[i]);
            return 1;
        }

        soma += notas[i];

        if (notas[i] > maior) maior = notas[i];
        if (notas[i] < menor) menor = notas[i];

        if (notas[i] >= 7)
            aprovados++;
        else if (notas[i] >= 5)
            recuperacao++;
        else
            reprovados++;
    }

    printf("Quantidade: %d\n", quantidade);
    printf("Media: %.2f\n", soma / quantidade);
    printf("Maior nota: %.2f\n", maior);
    printf("Menor nota: %.2f\n", menor);
    printf("Aprovados: %d\n", aprovados);
    printf("Recuperacao: %d\n", recuperacao);
    printf("Reprovados: %d\n", reprovados);

    return 0;
}
