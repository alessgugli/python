import sqlite3 

# crea la connessione ad un database
conn = sqlite3.connect("custom.db")

# crea il cursore con cui eseguire le query
c = conn.cursor()

# crea una table (le 6" servono per scrivere in piu righe)
# c.execute("""CREATE TABLE customers(
#     first_name text,
#     last_name text,
#     email text
# )""")

# inseriamo le righe nella table
# c.execute("""INSERT INTO customers VALUES
#             ('mario', 'rossi', 'mariorossi@gmail.com'),
#             ('gabriele', 'bianchi', 'gabrielebianchi@yahoo.it')""")

# ottenere dati dalla tabella
# c.execute("SELECT * FROM customers")
# righe = c.fetchall()
# for riga in righe:
#     print(riga)
#     # print(riga[0]) restituisce solo il primo valore di ogni riga, nel nostro caso il first_name

# ottenere dati specifici dalla tabella
# c.execute("SELECT * FROM customers WHERE first_name = 'mario'")
# print(c.fetchall())

# salva le modifiche
conn.commit()

# chiude la connessione
conn.close()
