def sistema_usuarios():
    usuarios = []

    while True:
        print("\n===== Sistema de Usuários =====")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print("\n--- Cadastro de usuário ---")
           
            while True:
                print("Escolha o tipo de perfil:")
                print("1 - Artista")
                print("2 - Professor")
                opcao = input("escolha uma das opção 1 ou 2: ")

                if opcao == "1":
                    tipo = "Artista"
                    break
                elif opcao == "2":
                    tipo = "Professor"
                    break
                else:
                    print("Opção inválida! Digite 1 ou 2.")

            while True:
                nome = input("Nome completo (máx. 50 caracteres): ")
                if nome.isalpha() and len(nome) <= 50:
                    break
                elif len(nome) > 50:
                    print("Nome muito longo!")
                else:
                    print("Digite apenas letras.")
                    
            while True:
                telefone = input("Telefone (máx. 15 caracteres): ")
                if telefone.isdigit() and len(telefone) <= 15:
                    break
                print("Telefone inválido! Digite apenas números e não ultrapasse 15 caracteres.")

            while True:
                email = input("E-mail (máx. 50 caracteres): ")
                if email and len(email) <= 50:
                    break
                print("E-mail inválido! Preencha corretamente e não ultrapasse 50 caracteres.")

            while True:
                senha = input("Senha (máx. 10 caracteres): ")
                if senha and len(senha) <= 10:
                    break
                print("Senha inválida! Preencha corretamente e não ultrapasse 10 caracteres.")

            usuario = {
                "tipo": tipo,
                "nome": nome,
                "telefone": telefone,
                "email": email,
                "senha": senha
            }
            usuarios.append(usuario)
            print(f"\nUsuário {nome} ({tipo}) cadastrado com sucesso!")

        elif escolha == "2":
            print("\n--- Login ---")
            email_login = input("E-mail: ")
            senha_login = input("Senha: ")
           
            encontrado = False
            for u in usuarios:
                if u['email'] == email_login and u['senha'] == senha_login:
                    print(f"\nLogin bem-sucedido! Bem-vindo(a), {u['nome']} ({u['tipo']})!")
                    encontrado = True
                    break
            if not encontrado:
                print("E-mail ou senha incorretos!")

        elif escolha == "3":
            print("Saindo do sistema de usuários...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema_usuarios()
