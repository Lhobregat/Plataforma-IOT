import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from joblib import dump


dados = pd.read_csv("dados_treinamento.csv") 


X = dados[["energia", "banda", "prioridade", "estabilidade"]]
y = dados["classe"] 


scaler = StandardScaler()
X_normalizado = scaler.fit_transform(X)


modelo = RandomForestClassifier()
modelo.fit(X_normalizado, y)


dump(modelo, "modelo_ia.joblib")
dump(scaler, "scaler.joblib")

print("Modelo e scaler treinados e salvos com sucesso.")
