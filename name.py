while True:
    nome_completo= input("Digite seu nome completo: ")

    try:
        ano_nascimento = int(input("Digite seu ano de nascimento (1922 a 2021): "))

        if 1922 <= ano_nascimento <= 2021:
            idade = 2022 - ano_nascimento
            print("\nNome:",nome_completo)
            print("Idade em 2022:",idade, "anos")
            break
        else:
            print("Erro: o ano deve estar entre 1922 e 2021.")

    except ValueError:
        print("Erro: digite um número válido para o ano.")