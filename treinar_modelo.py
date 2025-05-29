import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from joblib import dump

# Carregar dados de exemplo
dados = pd.read_csv("dados_treinamento.csv")  # Substitua pelo seu dataset real

# Features e alvo
X = dados[["energia", "banda", "prioridade", "estabilidade"]]
y = dados["classe"]  # Deve conter 0, 1 ou 2 para "econômico", "balanceado" e "performance"

# Normalizar os dados
scaler = StandardScaler()
X_normalizado = scaler.fit_transform(X)

# Treinar modelo
modelo = RandomForestClassifier()
modelo.fit(X_normalizado, y)

# Salvar modelo e scaler
dump(modelo, "modelo_ia.joblib")
dump(scaler, "scaler.joblib")

print("Modelo e scaler treinados e salvos com sucesso.")
