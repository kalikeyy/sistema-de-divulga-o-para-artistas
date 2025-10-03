def sistema_cursos():
    cursos = []

    while True:
        print("\n===== Cursos =====")
        print("1 - Criar curso")
        print("2 - Ver cursos cadastrados")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Criar novo curso ---")
           
            while True:
                nome = input("Nome do curso (máx. 50 caracteres): ")
                if len(nome) <= 50:
                    break
                print("Nome inválido! Tente novamente.")
           
            while True:
                professor = input("Nome do professor (máx. 30 caracteres): ")
                if professor.isalpha() and len(professor) <= 30:
                    break
                elif len(nome) > 30:
                    print("Nome muito longo!")
                else:
                    print("Digite apenas letras.")
           
            while True:
                try:
                    carga = int(input("Carga horária (em horas): "))
                    if carga > 0:
                        break
                    else:
                        print("Digite um valor positivo.")
                except ValueError:
                    print("Digite apenas números.")
           
            while True:
                descricao = input("Descrição do curso (máx. 200 caracteres): ")
                if len(descricao) <= 200:
                    break
                print("Descrição inválida! Tente novamente.")
           
            curso = {
                "nome": nome,
                "professor": professor,
                "carga_horaria": carga,
                "descricao": descricao
            }
            cursos.append(curso)
            print("\nCurso criado com sucesso!")

        elif opcao == "2":
            print("\n=== Cursos Cadastrados ===")
            if not cursos:
                print("Nenhum curso cadastrado ainda.")
            else:
                for i, c in enumerate(cursos, 1):
                    print(f"\n--- Curso {i} ---")
                    print(f"Nome: {c['nome']}")
                    print(f"Professor: {c['professor']}")
                    print(f"Carga horária: {c['carga_horaria']} horas")
                    print(f"Descrição: {c['descricao']}")

        elif opcao == "3":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema_cursos()
