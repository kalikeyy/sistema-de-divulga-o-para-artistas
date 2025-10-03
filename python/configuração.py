def configuracoes_conta():
    conta = {
        "nome": "Usuário Padrão",
        "telefone": "000000000",
        "email": "usuario@email.com",
        "senha": "1234"
    }

    while True:
        print("\n===== Configurações da Conta =====")
        print("1 - Alterar Nome")
        print("2 - Alterar Telefone")
        print("3 - Alterar E-mail")
        print("4 - Alterar Senha")
        print("5 - Ver Dados")
        print("6 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            while True:
                nome = input("Novo nome (somente letras, máx. 50 caracteres): ")
                if nome.isalpha() and len(nome) <= 50:
                    conta["nome"] = nome
                    print(f"Nome atualizado para {nome}!")
                    break
                elif len(nome) > 50:
                    print("Nome muito longo! Máx. 50 caracteres.")
                else:
                    print("Nome inválido! Use apenas letras.")

        elif escolha == "2":
            while True:
                telefone = input("Novo telefone (somente números, máx. 15 dígitos): ")
                if telefone.isdigit() and len(telefone) <= 15:
                    conta["telefone"] = telefone
                    print(f"Telefone atualizado para {telefone}!")
                    break
                print("Telefone inválido! Digite apenas números e até 15 dígitos.")

        elif escolha == "3":
            while True:
                email = input("E-mail (máx. 50 caracteres): ")
                if email and len(email) <= 50:
                    conta["email"] = email
                    print(f"E-mail atualizado para {email}!")
                    break
                print("E-mail inválido! Preencha corretamente e não ultrapasse 50 caracteres.")

        elif escolha == "4":
            while True:
                senha = input("Nova senha (máx. 10 caracteres): ")
                if senha and len(senha) <= 10:
                    conta["senha"] = senha
                    print("Senha atualizada com sucesso!")
                    break
                print("Senha inválida! Preencha corretamente (máx. 10 caracteres).")

        elif escolha == "5":
            print("\n=== Dados da Conta ===")
            for chave, valor in conta.items():
                print(f"{chave}: {valor}")

        elif escolha == "6":
            print("Saindo das configurações...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    configuracoes_conta()

