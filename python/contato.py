def sistema_contato():
    print("=== Fale Conosco ===")
   
    while True:
        email = input("Digite seu e-mail (máx. 150 caracteres): ")
        if len(email) <= 150:
            break
        print("E-mail inválido! Preencha corretamente e não ultrapasse 150 caracteres.")

    while True:
        mensagem = input("Digite sua mensagem ou pergunta (máx. 300 caracteres): ")
        if len(mensagem) <= 300:
            break
        print("Mensagem inválida! Preencha corretamente e não ultrapasse 300 caracteres.")

    print("\nEnviando mensagem...")
    print("Mensagem enviada com sucesso! Aguardaremos seu contato.")


if __name__ == "__main__":
    sistema_contato()
