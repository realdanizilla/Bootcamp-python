import pandas as pd
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "exemplo.csv")

print("Resolved file path:", file_path)
print("Does the file exist?", os.path.exists(file_path))


# lendo csv e filtrando df somente com comandos
df = pd.read_csv(file_path)

df_filtrado = df[df['estado'] == 'SP']

print(df_filtrado)
print()


# a mesma coisa, usando uma funcao

def ler_csv(file):
    df = pd.read_csv(file)
    df_filtrado = df[df['estado'] == 'SP']
    print(df_filtrado)
    print()
    return df_filtrado

arquivo_csv = file_path
ler_csv(arquivo_csv)


# a mesma coisa usando classe
class CSVProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
    
    def filtrar_por(self, coluna, atributo):
        return self.df[self.df[coluna] == atributo]
    

arquivo_csv = file_path
filtro = 'estado'
atributo = 'SP'

processador_csv = CSVProcessor(arquivo_csv)
processador_csv.carregar_csv()
print(processador_csv.filtrar_por(filtro,atributo))
print()

# porém como náo atribuimos o df filtrado a nenhuma variável, se charmarmos o df original ele nao terá o filtro

# agora usando um filtro que aceita multiplos valores de coluna e atributo usando recursividade
class CSVProcessor2:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df = None

    def carregar_csv(self):
        self.df = pd.read_csv(self.file_path)
    
    def filtrar_por(self, colunas, atributos):
        if len(colunas) != len(atributos):
            raise ValueError("Nao tem o mesmo numero de colunas e atributos")
        
        if len(colunas) == 0 or len(atributos) == 0:
            return self.df
        
        coluna_atual = colunas[0]
        atributo_atual = atributos[0]
        
        df_filtrado = self.df[self.df[coluna_atual] == atributo_atual]

        if len(colunas) == 1:
            return df_filtrado
        else:
            return self.filtrar_por(colunas[1:],atributos[1:])


processador_csv2 = CSVProcessor2(arquivo_csv)
processador_csv2.carregar_csv()
print(processador_csv2.filtrar_por(['estado', 'preco'], ['SP', '10,50']))