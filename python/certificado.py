def sistema_certificados():
    certificados = []

    while True:
        print("\n===== Emitir Certificados =====")
        print("1 - Emitir certificado")
        print("2 - Ver certificados emitidos")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Emitir novo certificado ---")
           
            while True:
                nome = input("Nome do aluno (máx. 50 caracteres): ")
                if nome.isalpha() and len(nome) <= 50:
                    break
                elif len(nome) > 50:
                    print("Nome muito longo!")
                else:
                    print("Digite apenas letras.")
           
            while True:
                curso = input("Nome do curso (máx. 50 caracteres): ")
                if len(curso) <= 50:
                    break
                print("Curso inválido! Tente novamente.")
           
            while True:
                data = input("Data de conclusão (dd/mm/aaaa): ")
                if len(data) == 10 and data[2] == "/" and data[5] == "/":
                    break
                print("Data inválida! Digite no formato dd/mm/aaaa.")
           
            certificado = {
                "nome": nome,
                "curso": curso,
                "data": data
            }
            certificados.append(certificado)
            print("\nCertificado emitido com sucesso!")
            print(f"\n--- CERTIFICADO ---")
            print(f"Certificamos que {nome} concluiu o curso '{curso}' em {data}.")
            print(f"Parabéns pela conquista!")

        elif opcao == "2":
            print("\n=== Certificados Emitidos ===")
            if not certificados:
                print("Nenhum certificado emitido ainda.")
            else:
                for i, cert in enumerate(certificados, 1):
                    print(f"\n--- Certificado {i} ---")
                    print(f"Aluno: {cert['nome']}")
                    print(f"Curso: {cert['curso']}")
                    print(f"Data de conclusão: {cert['data']}")

        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    sistema_certificados()

