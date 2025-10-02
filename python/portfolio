def sistema_portfolio():
    portfolio = []

    while True:
        print("\n===== Portfolio =====")
        print("1 - Criar post")
        print("2 - Ver portfólio")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Criar novo post ---")
            
            while True:
                titulo = input("Título da arte (máx. 50 caracteres): ")
                if len(titulo) <= 50:
                    break
                print("Título inválido! Tente novamente.")
            
            while True:
                autor = input("Nome do autor (máx. 30 caracteres): ")
                if len(autor) <= 30:
                    break
                print("Nome inválido! Tente novamente.")
            
            while True:
                categoria = input("Categoria (máx. 30 caracteres): ")
                if len(categoria) <= 30:
                    break
                print("Categoria inválida! Tente novamente.")
            
            while True:
                descricao = input("Descrição da arte (máx. 200 caracteres): ")
                if len(descricao) <= 200:
                    break
                print("Descrição muito longa! Tente novamente.")

            post = {
                "titulo": titulo,
                "autor": autor,
                "categoria": categoria,
                "descricao": descricao
            }
            portfolio.append(post)
            print("\nPost criado com sucesso!")

        elif opcao == "2":
            print("\n=== Portfólio de Artes Postadas ===")
            if not portfolio:
                print("Nenhum post foi feito ainda.")
            else:
                for i, post in enumerate(portfolio, 1):
                    print(f"\n--- Post {i} ---")
                    print(f"Título: {post['titulo']}")
                    print(f"Autor: {post['autor']}")
                    print(f"Categoria: {post['categoria']}")
                    print(f"Descrição: {post['descricao']}")

        elif opcao == "3":
            print("Saindo da plataforma...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema_portfolio()

