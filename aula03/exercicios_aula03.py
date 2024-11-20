# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])



# texto = "a raposa marrom salta sobre o cachorro marrom preguiçoso"
# palavras = texto.split()
# contagem_palavras = {}

# for palavra in palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# print(contagem_palavras)


# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)


# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

# print(usuarios_validos)


# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)



# Integre no arquivo do kpi um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

# solicita que o usuário informe o nome

nome_valido = False
salario_valido = False
bonus_valido = False

# loop para verificar o nome

while not nome_valido:
    try:
        nome = input("Qual seu nome?")

    # tratativa de erro
        if nome.isdigit():
            print("Você não digitou um nome, mas sim um número!")
            exit()
        elif len(nome) == 0:
            print("Voce não escreveu nada")
            exit()
        elif nome.isspace():
            print("Voce digitou um ou mais espaços, digite seu nome")
            exit()
        else:
            nome_valido = True
            print("nome ", nome)
    except ValueError as e:
        print(e)


while not salario_valido:
# solicita que o usuário informe o salário e converte para float
    try:
        salario = float(input("Qual seu salário?"))
        if salario < 0:
            print("Salário não pode ser negativo")
            exit()
        else:
            salario_valido = True
            print("salario: ", salario)

    except ValueError as e:
        print(e)
        exit()

    except TypeError as e:
        print(e)
        exit()

# solicita que o usuário informe o multiplicador do bonus e converte para float

while not bonus_valido:
    try:
        bonus = float(input("Qual seu bônus?"))
        if bonus < 0:
            print("Bônus não pode ser negativo")
            exit()
        else:
            bonus_valido = True
            print("O bonus é", bonus)

    except ValueError as e:
        print(e)
        exit()

# calcula o valor do bonus somando 1000 ao valor do bonus
bonus_valor = salario * bonus + 1000

# calcula o valor total a receber
total = salario + bonus_valor

# saúda o usuário e informa o total recebido e o bônus
print(f"Olá {nome} o total recebido é R$ {total:.2f} e seu bonus é de {bonus_valor:.1f}")