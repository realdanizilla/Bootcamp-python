
# 1. Inteiros (int)
# Métodos e operações:
# + (adição)
# - (subtração)
# * (multiplicação)
# // (divisão inteira)
# % (módulo - resto da divisão)

# 2. Números de Ponto Flutuante (float)
# Métodos e operações:
# + (adição)
# - (subtração)
# * (multiplicação)
# / (divisão)
# ** (potenciação)

# 3. Strings (str)
# Métodos e operações:
# .upper() (converte para maiúsculas)
# .lower() (converte para minúsculas)
# .strip() (remove espaços em branco no início e no final)
# .split(sep) (divide a string em uma lista, utilizando sep como delimitador)
# + (concatenação de strings)

# 4. Booleanos (bool)
# Operações lógicas:
# and (E lógico)
# or (OU lógico)
# not (NÃO lógico)
# == (igualdade)
# != (diferença)

# Inteiros (int)
# Escreva um programa que soma dois números inteiros inseridos pelo usuário.

try:
    num1 = int(input("insira um número"))
except NameError as e:
    print('erro, vc não informou um número ou informou um valor inválido')
    print(e)
    exit()
except TypeError as e:
    print(e)
    exit()
except ValueError as e:
    print(e)
    exit()

try:
    num2 = int(input("insira outro número"))
except NameError as e:
    print('erro, vc não informou um número ou informou um valor inválido')
    print(e)
    exit()
except TypeError as e:
    print(e)
    exit()
except ValueError as e:
    print(e)
    exit()

print(f"resultado é: {num1 + num2}")

# Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# Números de Ponto Flutuante (float)
# Escreva um programa que receba dois números flutuantes e realize sua adição.
# Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# Strings (str)
# Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# Escreva um programa que concatene duas strings fornecidas pelo usuário.

# Booleanos (bool)
# Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# Exercício 21: Conversor de Temperatura
# Escreva um programa que converta a temperatura de Celsius para Fahrenheit.
# O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, garantir que a entrada seja numérica,
# tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente,
# desconsiderando espaços e pontuações). Utilize try-except para garantir que a entrada seja uma string.
# Dica: Utilize a função isinstance() para verificar o tipo da entrada.

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas não numéricas.
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número.
# Utilize try-except para assegurar que a entrada seja numérica e
# utilize if-elif-else para classificar o número como "positivo", "negativo" ou "zero".
# Adicionalmente, identifique se o número é "par" ou "ímpar".

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula.
# O programa deve converter a string de entrada em uma lista de números inteiros.
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro.
# Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro.
# Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.
