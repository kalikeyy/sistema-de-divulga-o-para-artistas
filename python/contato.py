def sistema_contato():
    print("=== Fale Conosco ===")
   
    while True:
        email = input("Digite seu e-mail (máx. 50 caracteres): ")
        if len(email) <= 50:
            break
        print("E-mail inválido! Preencha corretamente e não ultrapasse 50 caracteres.")

    while True:
        mensagem = input("Digite sua mensagem ou pergunta (máx. 200 caracteres): ")
        if len(mensagem) <= 200:
            break
        print("Mensagem inválida! Preencha corretamente e não ultrapasse 200 caracteres.")

    print("\nEnviando mensagem...")
    print("Mensagem enviada com sucesso! Aguardaremos seu contato.")


if __name__ == "__main__":
    sistema_contato()
