from flask import Flask, render_template, request
import sqlite3
import hashlib
import time
from joblib import load
import numpy as np

# Inicializar banco de dados
conn = sqlite3.connect('iot_data.db') 
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS dados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dispositivo TEXT,
    energia REAL,
    banda REAL,
    prioridade REAL,
    estabilidade REAL,
    resultado TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS dispositivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dispositivo TEXT,
    tipo TEXT,
    localizacao TEXT,
    modelo TEXT,
    comunicacao TEXT,
    status TEXT
)
''')

conn.commit()
conn.close()

app = Flask(__name__)


modelo_ia = load('modelo_ia.joblib')
scaler = load('scaler.joblib') 


mapa_resultado_inverso = {0: "econômico", 1: "balanceado", 2: "performance"}


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256(
            (str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode()
        ).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), data, previous_block.hash)
        self.chain.append(new_block)

blockchain = Blockchain()

@app.route("/", methods=["GET", "POST"])
def index():

    conn = sqlite3.connect("iot_data.db")
    cursor = conn.cursor()


    cursor.execute("SELECT dispositivo FROM dispositivos")
    dispositivos = cursor.fetchall()


    conn.close()


    return render_template("index.html", dispositivos=dispositivos)

@app.route("/prever", methods=["POST"])
def prever():

    energia = float(request.form["energia"])
    banda = float(request.form["banda"])
    prioridade = float(request.form["prioridade"])
    estabilidade = float(request.form["estabilidade"])
    dispositivo = request.form["dispositivo"]

    conn = sqlite3.connect("iot_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT energia, banda, prioridade, estabilidade, resultado FROM dados WHERE dispositivo = ?", (dispositivo,))
    dispositivo_existente = cursor.fetchone()


    if dispositivo_existente:
        energia_anterior, banda_anterior, prioridade_anterior, estabilidade_anterior, resultado_anterior = dispositivo_existente
        modo_anterior = resultado_anterior
    else:
        energia_anterior = banda_anterior = prioridade_anterior = estabilidade_anterior = resultado_anterior = "Não disponível"
        modo_anterior = "Não disponível"
    

    entrada = np.array([[energia, banda, prioridade, estabilidade]])
    entrada_normalizada = scaler.transform(entrada)  
    pred = modelo_ia.predict(entrada_normalizada)[0]
    resultado = mapa_resultado_inverso[pred]

  
    if dispositivo_existente:
        cursor.execute("""
            UPDATE dados
            SET energia = ?, banda = ?, prioridade = ?, estabilidade = ?, resultado = ?
            WHERE dispositivo = ?
        """, (energia, banda, prioridade, estabilidade, resultado, dispositivo))
    else:
    
        cursor.execute("""
            INSERT INTO dados (dispositivo, energia, banda, prioridade, estabilidade, resultado)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (dispositivo, energia, banda, prioridade, estabilidade, resultado))

    conn.commit()
    conn.close()


    dados = {
        "dispositivo": dispositivo,
        "energia": energia,
        "banda": banda,
        "prioridade": prioridade,
        "estabilidade": estabilidade,
        "resultado": resultado
    }
    blockchain.add_block(str(dados))


    return render_template("resultado.html", 
                           dispositivo=dispositivo, 
                           modo_anterior=modo_anterior,
                           energia_anterior=energia_anterior, 
                           banda_anterior=banda_anterior,
                           prioridade_anterior=prioridade_anterior,
                           estabilidade_anterior=estabilidade_anterior,
                           resultado=resultado, 
                           energia=energia, 
                           banda=banda, 
                           prioridade=prioridade, 
                           estabilidade=estabilidade, 
                           hash=blockchain.get_latest_block().hash[:20])

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        # Recebe os dados
        dispositivo = request.form["dispositivo"]
        tipo = request.form["tipo"]
        localizacao = request.form["localizacao"]
        modelo = request.form["modelo"]
        comunicacao = request.form["comunicacao"]
        status = request.form["status"]

        conn = sqlite3.connect("iot_data.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dispositivos (dispositivo, tipo, localizacao, modelo, comunicacao, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (dispositivo, tipo, localizacao, modelo, comunicacao, status))
        conn.commit()
        conn.close()

        return render_template("cadastro_sucesso.html", dispositivo=dispositivo)
    
    return render_template("cadastro_produto.html")

if __name__ == "__main__":
    app.run(debug=True)
