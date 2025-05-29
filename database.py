import sqlite3

def init_db():
    conn = sqlite3.connect('iot_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS registros (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    dispositivo TEXT,
                    energia REAL,
                    banda REAL,
                    prioridade REAL,
                    estabilidade REAL,
                    decisao TEXT,
                    hash TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

def inserir_dado(dispositivo, energia, banda, prioridade, estabilidade, decisao, hash_valor):
    conn = sqlite3.connect('iot_data.db')
    c = conn.cursor()
    c.execute('''INSERT INTO registros (dispositivo, energia, banda, prioridade, estabilidade, decisao, hash)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (dispositivo, energia, banda, prioridade, estabilidade, decisao, hash_valor))
    conn.commit()
    conn.close()