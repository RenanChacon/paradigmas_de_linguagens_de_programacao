from funcoes import criar_vetor,valores,somaValoresVetor
def main():
    vetor = criar_vetor(8)

    x,y = valores()

    soma = somaValoresVetor(vetor,x,y)

    print(f"A soma dos valores nas posições x e y é {soma}")

# Exibir a soma dos elementos do Vetor com suas características principais.
if __name__ == "__main__":
    main()