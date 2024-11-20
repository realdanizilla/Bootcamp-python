# solicita que o usuário informe o nome
nome = input("Qual seu nome?")

# solicita que o usuário informe o salário e converte para float
salario = float(input("Qual seu salário?"))

# solicita que o usuário informe o multiplicador do bonus e converte para float
bonus = float(input("Qual seu bônus?"))

# calcula o valor do bonus somando 1000 ao valor do bonus
bonus_valor = salario * bonus + 1000

# calcula o valor total a receber
total = salario + bonus_valor

# saúda o usuário e informa o total recebido e o bônus
print(f"Olá {nome} o total recebido é {total} e seu bônus é {bonus_valor}")
