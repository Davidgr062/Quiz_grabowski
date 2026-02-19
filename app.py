import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Datenbank-Verbindung
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Startseite / Board anzeigen
@app.route('/')
def index():
    conn = get_db_connection()
    beitraege = conn.execute('SELECT * FROM beitraege').fetchall()
    conn.close()
    return render_template('index.html', beitraege=beitraege)

# Neue Nachricht hinzufügen
@app.route('/add', methods=['POST'])
def add_post():
    autor = request.form.get('autor')
    titel = request.form.get('titel')
    inhalt = request.form.get('inhalt')

    if autor and titel and inhalt:
        conn = get_db_connection()
        conn.execute("INSERT INTO beitraege (autor, titel, inhalt) VALUES (?, ?, ?)",
                     (autor, titel, inhalt))
        conn.commit()
        conn.close()

    return redirect(url_for('index'))

# Nachricht löschen
@app.route('/delete/<int:id>', methods=['POST'])
def delete_post(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM beitraege WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
