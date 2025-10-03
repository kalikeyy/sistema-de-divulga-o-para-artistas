def avaliar_curso():
    avaliacoes = []

    print("=== Avalie seu Curso ===")
    while True:
        curso = input("\nDigite o nome do curso que deseja avaliar (máx. 30 caracteres): ")
        if curso.isalpha() and len(curso) <= 30:
            break
        elif len(curso) > 30:
            print("Nome do curso muito longo!")
        else:
            print("Digite apenas letras.")

    while True:
        try:
            nota = int(input("Dê uma nota de 1 a 5: "))
            if 1 <= nota <= 5:
                break
            else:
                print("Digite um número entre 1 e 5.")
        except ValueError:
            print("Digite apenas números.")

    while True:
        comentario = input("Escreva um comentário (máx. 100 caracteres): ")
        if len(comentario) <= 100:
            break
        else:
            print("Comentário muito longo!")

    avaliacao = {"nota": nota, "comentario": comentario}
    avaliacoes.append(avaliacao)

    print(f"\n=== Avaliações do curso: {curso} ===")
    soma_notas = 0
    for i, av in enumerate(avaliacoes, 1):
        print(f"\n--- Avaliação {i} ---")
        print(f"Nota: {av['nota']}/5")
        print(f"Comentário: {av['comentario']}")
        soma_notas += av['nota']

    if avaliacoes:
        media = soma_notas / len(avaliacoes)
        print(f"\nNota média do curso: {media:.1f}/5")

avaliar_curso()

