import sqlite3
from hash_generator import sha256_gen
from webhook import sendWebhook, WEBHOOK_URL


conn = sqlite3.connect('fish.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS hash_value (
    id INTEGER PRIMARY KEY,
    hash TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS plain_text (
    id INTEGER PRIMARY KEY,
    text TEXT NOT NULL
)
''')

filename = "rockyou.txt"
with open(filename, 'r') as file:
    for line in file:
        hash_value = sha256_gen(line)    
        try:
            cursor.execute(f"INSERT INTO hash_value (hash) VALUES ('{hash_value}')")
            cursor.execute(f"INSERT INTO plain_text (text) VALUES ('{line}')")
            conn.commit()
            message = f"Added {hash_value} And {line} Into Database"
            print(message)
            sendWebhook(WEBHOOK_URL, message, "fish database guard", "https://thebtlgfish.github.io/images/cat.jpeg")
        except Exception as e:
            print(f"An error occurred: {e}")

print("Hash Values:")
cursor.execute("SELECT * FROM hash_value")
hash_rows = cursor.fetchall()

for row in hash_rows:
    print(row)

print("\nPlain Texts:")
cursor.execute("SELECT * FROM plain_text")
text_rows = cursor.fetchall()

for row in text_rows:
    print(row)

conn.close()
