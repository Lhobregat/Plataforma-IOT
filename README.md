# Plataforma-IOT
Plataforma Inteligente IoT com Blockchain e IA
Este projeto é uma simulação de uma plataforma web inteligente para redes IoT que utiliza aprendizado de máquina (IA) para tomada de decisão dinâmica e Blockchain para registrar eventos de forma segura e rastreável.

🔧 Tecnologias Utilizadas
Python (Flask) – Backend e API da plataforma

HTML + CSS + JavaScript – Interface Web

SQLite – Banco de dados local

Scikit-learn – Treinamento do modelo de IA

Joblib – Salvamento e carregamento do modelo IA

CryptoJS – Geração de hash criptográfico no frontend

Blockchain Simulada – Registro de decisões e entradas

📈 Funcionalidades
Cadastro de dispositivos IoT (tipo, localização, modelo, etc.)

Formulário para enviar dados contextuais:
Energia, Banda, Prioridade, Estabilidade

Sistema de IA (pré-treinado) que recomenda o melhor modo de operação:

Econômico

Balanceado

Alta Performance

Registro das decisões em uma Blockchain simulada com geração de hash

Armazenamento de histórico de decisões em banco de dados

Exibição de decisão anterior do dispositivo

📂 Estrutura do Projeto
graphql
Copiar
Editar
Plataforma-IOT/
│
├── main.py                 # App Flask principal
├── treinar_modelo.py       # Script para treinar o modelo IA
├── modelo_ia.joblib        # Modelo IA treinado
├── scaler.joblib           # Scaler (normalizador) dos dados
├── iot_data.db             # Banco SQLite com dispositivos e dados
├── templates/
│   ├── index.html          # Página principal (formulário)
│   ├── resultado.html      # Página com a decisão da IA e hash
│   └── cadastro_produto.html  # Formulário de cadastro de dispositivos
├── static/
│   └── style.css           # Estilo das páginas
├── blockchain.py           # Lógica da blockchain
├── database.py             # (opcional) Criação de tabelas
├── dadostreinamento.py     # Gera dados simulados de treino
└── dados_treinamento.csv   # CSV com dados históricos para IA
🚀 Como Executar
1. Instalar dependências:
bash
pip install flask scikit-learn joblib numpy

3. Treinar a IA (opcional):
python treinar_modelo.py

5. Iniciar a plataforma:
python main.py

Acesse no navegador:
http://127.0.0.1:5000

📊 Exemplo de Fluxo
Usuário cadastra um dispositivo IoT.

Ele informa as variáveis (energia, banda, etc.).

A IA prevê o melhor modo de operação.

A decisão é salva no banco e registrada na blockchain simulada.

O usuário vê o modo atual, o anterior e o hash de verificação.

🔐 Sobre a Blockchain
Cada novo conjunto de dados enviados forma um bloco com:

Índice

Timestamp

Dados

Hash do bloco anterior

Hash criptográfico SHA-256

Isso garante imutabilidade e rastreabilidade das decisões tomadas.

🤖 Inteligência Artificial
Utiliza um modelo supervisionado (ex: RandomForest).

Os dados são normalizados com StandardScaler.

O modelo é treinado com base em diferentes cenários e gravado com joblib.

📌 Possíveis Expansões
Integração com Blockchain real (Ganache ou Ethereum via Web3.py)

Treinamento contínuo com DRL (Deep Reinforcement Learning)

Painel visual com gráficos (usando Chart.js)

Sistema de autenticação de usuários

Previsão de falhas com IA

👨‍💻 Autores
Guilherme

Vinícius

Gustavo
