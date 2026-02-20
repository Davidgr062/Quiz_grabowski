import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / 'database.db'

SCHEMA = '''
CREATE TABLE IF NOT EXISTS beitraege (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    autor TEXT NOT NULL,
    titel TEXT NOT NULL,
    inhalt TEXT NOT NULL,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS schueler (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    klasse TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS text_quiz (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    frage1 TEXT NOT NULL,
    antwort1 TEXT NOT NULL,
    frage2 TEXT NOT NULL,
    antwort2 TEXT NOT NULL
);
'''

def init_db(path: Path):
    conn = sqlite3.connect(str(path))
    cur = conn.cursor()
    cur.executescript(SCHEMA)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db(DB_PATH)
    print(f'Datenbank initialisiert bei: {DB_PATH}')
