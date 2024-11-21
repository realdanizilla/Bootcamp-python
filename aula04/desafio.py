lista: list = []

def cadastrar_usuario_salario_bonus():
    db: dict = {}
    nome_valido = False
    salario_valido = False
    bonus_valido = False

    # loop para verificar o nome

    while not nome_valido:
        try:
            nome: str = input("Qual seu nome?")

        # tratativa de erro
            if nome.isdigit():
                print("Você não digitou um nome, mas sim um número!")

            elif len(nome) == 0:
                print("Voce não escreveu nada")

            elif nome.isspace():
                print("Voce digitou um ou mais espaços, digite seu nome")

            else:
                nome_valido = True
                print("nome ", nome)

        except ValueError as e:
            print(e)


    while not salario_valido:
    # solicita que o usuário informe o salário e converte para float
        try:
            salario: float = float(input("Qual seu salário?"))
            if salario < 0:
                print("Salário não pode ser negativo")

            else:
                salario_valido = True
                print("salario: ", salario)

        except ValueError as e:
            print(e)

        except TypeError as e:
            print(e)


    # solicita que o usuário informe o multiplicador do bonus e converte para float

    while not bonus_valido:
        try:
            bonus: float = float(input("Qual seu bônus?"))
            if bonus < 0:
                print("Bônus não pode ser negativo")

            else:
                bonus_valido = True
                print("O bonus é", bonus)

        except ValueError as e:
            print(e)


    # calcula o valor do bonus somando 1000 ao valor do bonus
    bonus_valor: float = salario * bonus + 1000

    # calcula o valor total a receber
    total: float = salario + bonus_valor

    # gerar informações no dicionario db
    db["nome"] = nome
    db["salario"] = salario
    db["bonus"] = bonus_valor
    db["total"] = total

    # adicionar informações à lista
    lista.append(db)

    # saúda o usuário e informa o total recebido e o bônus
    print(f"Olá {nome} o total recebido é R$ {total:.0f} e seu bonus é de {bonus_valor:.0f}")
    print(db)
    print(lista)

    # continuar ou sair
    continua: str = input("continuar? (y/n)")
    if continua == "y":
        cadastrar_usuario_salario_bonus()
    else:
        exit()

cadastrar_usuario_salario_bonus()