nome = input("Qual seu nome?")
salario = float(input("Qual seu salário?"))
bonus = float(input("Qual seu bônus?"))
bonus_valor = salario * bonus + 1000
total = salario + bonus_valor


print(f"Olá {nome} o total recebido é {total} e seu bônus é {bonus_valor}")
