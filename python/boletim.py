def sistema_boletim():
    boletins = []

    while True:
        print("\n===== Sistema de Boletim =====")
        print("1 - Adicionar boletim")
        print("2 - Ver boletins")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Adicionar novo boletim ---")

            while True:
                nome = input("Nome do aluno (máx. 50 caracteres):")
                if nome.isalpha() and len(nome) <= 50:
                    break
                elif len(nome) > 50:
                    print("Nome muito longo!")
                else:
                    print("Digite apenas letras.")

            notas = []
            for i in range(1, 4): 
                while True:
                    try:
                        nota = float(input(f"Digite a nota {i} (0 a 10): "))
                        if 0 <= nota <= 10:
                            notas.append(nota)
                            break
                        else:
                            print("Nota inválida! Digite entre 0 e 10.")
                    except ValueError:
                        print("Digite apenas números.")

            nota_final = sum(notas) / len(notas)

            if nota_final >= 7:
                status = "Aprovado"
            elif 5 <= nota_final < 7:
                status = "Em andamento"
            else:
                status = "Reprovado"

            while True:
                data = input("Data de emissão (dd/mm/aaaa): ")
                if len(data) == 10 and data[2] == "/" and data[5] == "/":
                    break
                print("Data inválida! Digite no formato dd/mm/aaaa.")

            boletim = {
                "nome": nome,
                "notas": notas,
                "nota_final": nota_final,
                "status": status,
                "data": data
            }
            boletins.append(boletim)
            print("\nBoletim adicionado com sucesso!")

        elif opcao == "2":
            print("\n=== Boletins Registrados ===")
            if not boletins:
                print("Nenhum boletim registrado ainda.")
            else:
                for i, b in enumerate(boletins, 1):
                    print(f"\n--- Boletim {i} ---")
                    print(f"Aluno: {b['nome']}")
                    print(f"Notas: {b['notas']}")
                    print(f"Nota final: {b['nota_final']}")
                    print(f"Status: {b['status']}")
                    print(f"Data de emissão: {b['data']}")

        elif opcao == "3":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema_boletim()

