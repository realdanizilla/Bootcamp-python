import pandas as pd
import numpy as np

# função para criar df com 100.000 linhas e 20 cidades
def criar_medidas(num_linhas=100000,num_cidades=20,semente=None):
    estado = np.random.RandomState(semente)
    cidades = [f"Cidade_{i}" for i in range(num_cidades)]
    dados = {
        "estacao": estado.choice(cidades,size=num_linhas),
        "medida":estado.uniform(-20,50,size=num_linhas).round(4)
    }
    df =pd.DataFrame(dados)
    return df

# criar df exemplo
df =criar_medidas(semente=0)

# exibir tipo de dados e memória antes
print("tipos de dados e uso de memória antes da conversão")
print(df.dtypes)
print(df.memory_usage(deep=True))

# salvar uso de memória inicial
uso_memoria_inicial = df.memory_usage(deep=True).sum()

# detalhes memória antes
detalhes_memoria_antes = df.memory_usage(deep=True)

# converter dados para tipos mais eficientes

df["estacao"] = df["estacao"].astype("category")
df["medida"] = pd.to_numeric(df['medida'],downcast="float")

# exibir tipo de dados e memória depois

print('\nTipos de dados e uso de memória após conv ersão:')
print(df.dtypes)
print(df.memory_usage(deep=True))

#salvar uso de memória final
uso_memoria_final = df.memory_usage(deep=True).sum()

# calcular redução no uso de memoria
reducao_total = 1 - (uso_memoria_final / uso_memoria_inicial)
reducao_estacao = 1 - (df.memory_usage(deep=True)['estacao'] / detalhes_memoria_antes['estacao'])
reducao_medida = 1 - (df.memory_usage(deep=True)['medida'] / detalhes_memoria_antes['medida'])

print(f"\nRedução total no uso de memoria: {reducao_total:.2f}")
print(f"redução em estação: {reducao_estacao:.2f}")
print(f"redução em medida: {reducao_medida:.2f}")

print("\nDetalhes uso de memória antes:")
print(detalhes_memoria_antes)

print('\nDetalhes uso de memória depois:')
print(df.memory_usage(deep=True))