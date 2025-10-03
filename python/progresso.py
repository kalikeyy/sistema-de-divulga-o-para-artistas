def sistema_progresso():
    progresso_alunos = []

    while True:
        print("\n===== Progresso do Aluno =====")
        print("1 - Registrar progresso")
        print("2 - Ver progresso")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Registrar novo progresso ---")

            while True:
                nome = input("Nome do aluno (máx. 50 caracteres): ")
                if nome.isalpha() and len(nome) <= 50:
                    break
                elif len(nome) > 50:
                    print("Nome muito longo!")
                else:
                    print("Digite apenas letras.")

            status_opcoes = ["Em andamento", "Concluído", "Reprovado", "Aprovado"]
            while True:
                status = input(f"Status do aluno {status_opcoes}: ").title()
                if status in status_opcoes:
                    break
                print(f"Status inválido! Escolha entre {status_opcoes}.")

            while True:
                try:
                    tempo = float(input("Tempo estudado (em horas): "))
                    if tempo >= 0:
                        break
                    else:
                        print("Digite um valor positivo.")
                except ValueError:
                    print("Digite apenas números.")

            while True:
                data_inicio = input("Data de início (dd/mm/aaaa): ")
                if len(data_inicio) == 10 and data_inicio[2] == "/" and data_inicio[5] == "/":
                    break
                print("Data inválida! Digite no formato dd/mm/aaaa.")

            while True:
                data_fim = input("Data de fim (dd/mm/aaaa): ")
                if len(data_fim) == 10 and data_fim[2] == "/" and data_fim[5] == "/":
                    break
                print("Data inválida! Digite no formato dd/mm/aaaa.")

            registro = {
                "nome": nome,
                "status": status,
                "tempo_estudado": tempo,
                "data_inicio": data_inicio,
                "data_fim": data_fim
            }
            progresso_alunos.append(registro)
            print("\nProgresso registrado com sucesso!")

        elif opcao == "2":
            print("\n=== Progresso dos Alunos ===")
            if not progresso_alunos:
                print("Nenhum registro encontrado.")
            else:
                for i, reg in enumerate(progresso_alunos, 1):
                    print(f"\n--- Registro {i} ---")
                    print(f"Aluno: {reg['nome']}")
                    print(f"Status: {reg['status']}")
                    print(f"Tempo estudado: {reg['tempo_estudado']} horas")
                    print(f"Data de início: {reg['data_inicio']}")
                    print(f"Data de fim: {reg['data_fim']}")

        elif opcao == "3":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema_progresso()
