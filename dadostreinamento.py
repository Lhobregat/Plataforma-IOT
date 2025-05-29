import pandas as pd

# Dados simulados
dados = {
    "energia": [20, 25, 40, 45, 70, 80],
    "banda": [15, 18, 30, 35, 50, 55],
    "prioridade": [30, 40, 60, 65, 90, 95],
    "estabilidade": [10, 12, 25, 28, 45, 50],
    "classe": [0, 0, 1, 1, 2, 2]
}

df = pd.DataFrame(dados)

# Salvar
df.to_csv("dados_treinamento.csv", index=False)

print("Arquivo 'dados_treinamento.csv' criado com sucesso!")