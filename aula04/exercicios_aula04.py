# type hint - é uma boa prática para tipagem estática
nome = "Alice"
nome_com_hint: str = "Jonas"

# type hint não muda nada em relação a validação e tratamento de erros

# json é um dicionario de javascript com algumas pequenas diferenças com  dict python. Usar json.dumps json.loads
# comunicação entre back end e front end normalmente é feita com json

# Exercícios de Listas e Dicionários
# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
lista: list = []
for i in range(1,11):
    print(i**2)
print()


# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista2: list = ["Python", "Java", "C++", "JavaScript"]
lista2.pop(2)
lista2.append("Ruby")
print(lista2)
print()


# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
dict1: dict = {
    "título": "Senhor dos Anéis",
    "autor": "J.R.R. Tolkien",
    "ano_publicação": 1954
}
for k,v in dict1.items():
    print(k,v)
print()


# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
string: str = "Python é uma linguagem de programação"
def contar_caracteres(string):
    ocorrencias = {}
    for caractere in string:
        ocorrencias[caractere] = ocorrencias.get(caractere,0) +1
    return ocorrencias
print(contar_caracteres(string))
print()


# Dada a lista ["maçã", "banana", "cereja"] 
# e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_compras: list = ["maçã", "banana", "cereja"]
precos: dict = {"maçã": 0.45, "banana": 0.30, "cereja":0.65}
def calcular_preco(lista_compras, precos):
    total = 0
    for item in lista_compras:
        total += precos[item]
    return total
print(calcular_preco(lista_compras,precos))
print()


#Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)
print()


#Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)
print()


# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)
print()


#Objetivo: Dado um conjunto de números, calcular a média.

numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)

print("Média:", media)
print()


#Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)
print()


#Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)
print()


# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)
print()


#Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)
print()


# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)