# solicita que o usuário informe o nome
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
except ValueError as e:
    print(e)


# solicita que o usuário informe o salário e converte para float
try:
    salario = float(input("Qual seu salário?"))
    if salario < 0:
        print("Salário não pode ser negativo")
        exit()

except ValueError as e:
    print(e)
    exit()

except TypeError as e:
    print(e)
    exit()

# solicita que o usuário informe o multiplicador do bonus e converte para float

try:
    bonus = float(input("Qual seu bônus?"))
    if bonus < 0:
        print("Bônus não pode ser negativo")
        exit()

except ValueError as e:
    print(e)
    exit()

# calcula o valor do bonus somando 1000 ao valor do bonus
bonus_valor = salario * bonus + 1000

# calcula o valor total a receber
total = salario + bonus_valor

# saúda o usuário e informa o total recebido e o bônus
print(f"Olá {nome} o total recebido é R$ {total:.2f} e seu bonus é de {bonus_valor:.1f}")
